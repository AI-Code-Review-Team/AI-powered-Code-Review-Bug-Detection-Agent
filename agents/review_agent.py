import openai
import json
import os
import time

client = openai.OpenAI(api_key=os.environ["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
"])

SYSTEM_PROMPT = """You are an expert Python code reviewer.
Analyze the given Python function and detect ALL of the following issues:

1. SECURITY issues (OWASP Top 10):
   - SQL injection (f-strings or concatenation in queries)
   - Hardcoded secrets (API keys, passwords in code)
   - Command injection (os.system with user input)
   - Path traversal (open() with user-controlled filenames)
   - Use of eval() or exec() with user input

2. PERFORMANCE issues:
   - N+1 database queries (query inside a loop)
   - Nested loops on large data (O(n²) complexity)
   - Missing caching on repeated expensive calls
   - String concatenation inside loops (use join instead)

3. STYLE issues (PEP8):
   - Missing function docstrings
   - Variable names that violate naming conventions
   - Lines longer than 120 characters
   - Unused imports

EXAMPLE INPUT:
def get_user(uid):
    query = f"SELECT * FROM users WHERE id = {uid}"
    cursor.execute(query)

EXAMPLE OUTPUT:
[{"line_start": 2, "line_end": 2,
  "category": "SECURITY",
  "severity": "CRITICAL",
  "type": "SQL_INJECTION",
  "description": "User input directly concatenated into SQL query.",
  "suggested_fix": "cursor.execute('SELECT * FROM users WHERE id = ?', (uid,))",
  "confidence": "HIGH"}]

Return ONLY a valid JSON array. No explanation. No markdown. No extra text.
If no issues found, return exactly: []

Each finding MUST have:
- line_start, line_end
- category (SECURITY / PERFORMANCE / STYLE)
- severity (CRITICAL / HIGH / MEDIUM / LOW / INFO)
- type
- description
- suggested_fix
- confidence (HIGH / MEDIUM / LOW)
"""

def review_agent(chunk: dict) -> list:
    """
    Single unified review agent.
    Detects security, performance, and style issues in one LLM call.
    Input:  chunk dict with 'source_code' and 'file' keys
    Output: list of finding dicts
    """
    code = chunk.get("source_code", "")
    file = chunk.get("file", "unknown")

    # Token budget check
    estimated_tokens = len(code.split()) * 1.3
    if estimated_tokens > 3000:
        code = " ".join(code.split()[:2300])
        print(f"[Review Agent] Warning: chunk truncated in {file}")

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": f"Review this Python function:\n\n{code}"}
            ],
            temperature=0.1,
            max_tokens=1500
        )

        raw = response.choices[0].message.content.strip()
        raw = raw.replace("```json", "").replace("```", "").strip()

        findings = json.loads(raw)

        for f in findings:
            f["file"] = file
            f["agent"] = "review"

        print(f"[Review Agent] Tokens used: {response.usage.total_tokens}")
        print(f"[Review Agent] Found {len(findings)} issue(s) in {file}")
        return _validate(findings, file)

    except json.JSONDecodeError:
        print(f"[Review Agent] Bad JSON, retrying...")
        return _retry(code, file)

    except openai.RateLimitError:
        print("[Review Agent] Rate limit hit. Waiting 60s...")
        time.sleep(60)
        return review_agent(chunk)

    except Exception as e:
        print(f"[Review Agent] Error: {e}")
        return []

def _retry(code: str, file: str) -> list:
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": f"Review this Python function. Return ONLY JSON array:\n\n{code}"}
            ],
            temperature=0.1,
            max_tokens=1500
        )
        raw = response.choices[0].message.content.strip()
        raw = raw.replace("```json", "").replace("```", "").strip()
        findings = json.loads(raw)
        for f in findings:
            f["file"] = file
            f["agent"] = "review"
        return _validate(findings, file)
    except Exception:
        return []

def _validate(findings: list, file: str) -> list:
    required = ["line_start", "severity", "category", "type", "description", "suggested_fix"]
    valid_severities = {"CRITICAL", "HIGH", "MEDIUM", "LOW", "INFO"}
    valid_categories = {"SECURITY", "PERFORMANCE", "STYLE"}
    validated = []
    for f in findings:
        for field in required:
            if field not in f:
                f[field] = "unknown"
        if f["severity"].upper() not in valid_severities:
            f["severity"] = "MEDIUM"
        if f.get("category", "").upper() not in valid_categories:
            f["category"] = "SECURITY"
        validated.append(f)
    return validated

# LangGraph compatible node
def review_node(state: dict) -> dict:
    chunks = state.get("chunks", [])
    all_findings = []
    for chunk in chunks:
        findings = review_agent(chunk)
        all_findings.extend(findings)
    # Sort by severity
    severity_order = {"CRITICAL": 0, "HIGH": 1, "MEDIUM": 2, "LOW": 3, "INFO": 4}
    all_findings.sort(key=lambda x: severity_order.get(x.get("severity", "INFO"), 4))
    return {**state, "findings": all_findings}

if __name__ == "__main__":
    for path in [
        "tests/test_fixtures/test_vuln_1.py",
        "tests/test_fixtures/test_vuln_2.py",
        "tests/test_fixtures/test_vuln_3.py",
    ]:
        print(f"\n{'='*50}\nTesting: {path}\n{'='*50}")
        chunk = {"file": path, "source_code": open(path).read()}
        results = review_agent(chunk)
        print(json.dumps(results, indent=2))
