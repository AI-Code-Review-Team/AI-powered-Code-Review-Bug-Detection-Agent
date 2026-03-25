import openai
import json
import os

client = openai.OpenAI(api_key=os.environ["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
"])

SYSTEM_PROMPT = """You are an expert Python security code reviewer.
Analyze the given Python function for security vulnerabilities.
Focus on OWASP Top 10: SQL injection, hardcoded secrets, command injection,
path traversal, insecure deserialization, broken authentication.

Respond ONLY with a valid JSON array. No explanation, no markdown.
Each item must have: line_start, line_end, severity (CRITICAL/HIGH/MEDIUM/LOW),
type, description, suggested_fix, confidence (HIGH/MEDIUM/LOW).
If no issues found, return: []
"""

def security_agent(chunk: dict) -> list:
    code = chunk.get("source_code", "")
    file = chunk.get("file", "unknown")

    user_msg = f"Analyze this Python function for security issues:\n\n{code}"

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user",   "content": user_msg}
            ],
            temperature=0.1,
            max_tokens=1000
