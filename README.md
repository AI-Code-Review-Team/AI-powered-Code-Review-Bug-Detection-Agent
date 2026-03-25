# 🤖 AI-Powered Code Review & Bug Detection Agent

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![LangGraph](https://img.shields.io/badge/LangGraph-Multi--Agent-7F77DD?style=for-the-badge)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o-412991?style=for-the-badge&logo=openai&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15+-336791?style=for-the-badge&logo=postgresql&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub-Webhooks-181717?style=for-the-badge&logo=github&logoColor=white)

**An autonomous multi-agent system that reviews Pull Requests for security vulnerabilities, performance anti-patterns, and style issues — posting inline comments directly to GitHub.**

[Features](#-features) · [Architecture](#-architecture) · [Setup](#-setup) · [Team](#-team) · [Demo](#-demo)

</div>

---

## 📖 Problem Statement

Senior developers spend **5–10 hours per week** manually reviewing pull requests. This creates bottlenecks in the development pipeline, delays shipping, and pulls senior engineers away from high-value work.

This project builds an AI-powered bot that:
- Intercepts every Pull Request via GitHub Webhooks
- Parses code changes using **tree-sitter** AST parsing (reducing token usage by ~95%)
- Routes code chunks through **three parallel LLM agents** via LangGraph
- Posts actionable inline review comments directly on the PR — with suggested fixes

> 💡 **Business Impact:** At $150/hr, automating even 5 hours/week of senior dev review time saves **$750–$1,500 per developer per week.**

---

## ✨ Features

| Feature | Description |
|---|---|
| 🔗 **GitHub Webhook Integration** | Triggers automatically on PR open, update, and re-open events |
| 🌳 **AST-Based Code Parsing** | Uses tree-sitter to extract only modified functions/classes — not raw diffs |
| 🔐 **Security Agent** | Detects OWASP Top 10 vulnerabilities: SQL injection, hardcoded secrets, command injection, path traversal |
| ⚡ **Performance Agent** | Catches N+1 queries, O(n²) loops, blocking async calls, repeated computations |
| 🎨 **Style Agent + RAG** | Enforces PEP8 and team coding guidelines using a RAG knowledge base |
| 🧠 **LangGraph Orchestrator** | Runs all 3 agents in parallel, deduplicates findings, prioritizes by severity |
| 💬 **Inline PR Comments** | Posts findings as GitHub review comments with Markdown-formatted suggested fixes |
| 📊 **Quality Dashboard** | Tracks team-level quality trends: findings by type, severity, and PR over time |
| 🔄 **Iterative Review** | On new commits, only re-analyzes the files that actually changed |

---

## 🏗 Architecture

```
GitHub Pull Request
        │
        ▼
┌───────────────────┐
│   GitHub Webhook  │  POST /webhook
│   (signed HMAC)   │
└────────┬──────────┘
         │
         ▼
┌───────────────────┐
│   FastAPI Server  │  Validates signature, fetches PR diff
│   + PostgreSQL    │  Stores PRs and findings
└────────┬──────────┘
         │
         ▼
┌───────────────────┐
│  Tree-sitter AST  │  Parses diff → semantic chunks
│     Parser        │  (functions, classes only)
└────────┬──────────┘
         │
         ▼
┌────────────────────────────────────────────┐
│            LangGraph Orchestrator          │
│                                            │
│  ┌─────────────┐  ┌──────────────────┐    │
│  │  Security   │  │  Performance     │    │  ← runs in parallel
│  │   Agent     │  │    Agent         │    │
│  └─────────────┘  └──────────────────┘    │
│         │                  │              │
│         ▼                  ▼              │
│  ┌─────────────┐  ┌──────────────────┐    │
│  │    Style    │  │   Merge Node     │    │
│  │  Agent+RAG  │  │  (deduplicate +  │    │
│  └─────────────┘  │   prioritize)    │    │
│                   └──────────────────┘    │
└────────────────────────────────────────────┘
         │
         ▼
┌───────────────────┐
│   GitHub API      │  Posts inline review comments
│   Inline Comments │  with suggested fixes
└───────────────────┘
         │
         ▼
┌───────────────────┐
│ Quality Dashboard │  Team trend charts
└───────────────────┘
```

### Why AST Parsing?

Instead of sending the entire diff to the LLM (which may be 10,000+ tokens), tree-sitter extracts only the **modified functions and classes**:

```
Raw PR diff:     ~8,000 tokens
After chunking:  ~400 tokens per function
Reduction:       ~95% fewer tokens = lower cost + better focus
```

---

## 🛠 Tech Stack

| Layer | Technology |
|---|---|
| **API Server** | FastAPI + Uvicorn |
| **Database** | PostgreSQL + SQLAlchemy |
| **Code Parsing** | tree-sitter + tree-sitter-python |
| **AI Agents** | OpenAI GPT-4o-mini / Anthropic Claude |
| **Orchestration** | LangGraph |
| **RAG Pipeline** | LangChain + ChromaDB |
| **GitHub Integration** | GitHub Apps API + Webhooks |
| **Tunnel (dev)** | ngrok |

---

## 📁 Project Structure

```
ai-code-review-agent/
│
├── app/
│   ├── main.py               # FastAPI app, webhook endpoint
│   ├── models.py             # SQLAlchemy DB models
│   ├── schemas.py            # Pydantic request/response schemas
│   └── database.py           # DB connection + session
│
├── agents/
│   ├── security_agent.py     # OWASP vulnerability detection (Member 5)
│   ├── performance_agent.py  # N+1, complexity detection (Member 6)
│   └── style_agent.py        # PEP8 + RAG style review (Member 7)
│
├── orchestrator/
│   └── graph.py              # LangGraph state machine (Member 8)
│
├── parser/
│   └── chunker.py            # tree-sitter AST parser (Member 4)
│
├── rag/
│   └── knowledge_base.py     # ChromaDB vector store + retrieval
│
├── github/
│   ├── webhook.py            # Signature verification, event handling
│   ├── diff_fetcher.py       # Fetch PR diff via GitHub API
│   └── commenter.py          # Post inline review comments
│
├── dashboard/
│   ├── routes.py             # Dashboard API endpoints
│   └── static/               # HTML + Chart.js dashboard
│
├── tests/
│   ├── test_security_agent.py
│   ├── test_performance_agent.py
│   ├── test_parser.py
│   └── test_fixtures/        # Intentionally vulnerable Python files
│
├── .env.example              # Environment variable template
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup

### Prerequisites

- Python 3.11+
- PostgreSQL 15+
- A GitHub account
- An OpenAI API key (or Anthropic API key)
- ngrok (for local webhook testing)

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-code-review-agent.git
cd ai-code-review-agent
```

### 2. Create a virtual environment and install dependencies

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Set up environment variables

```bash
cp .env.example .env
```

Edit `.env` with your credentials:

```env
# GitHub App
GITHUB_APP_ID=your_app_id
GITHUB_APP_PRIVATE_KEY_PATH=./private-key.pem
GITHUB_WEBHOOK_SECRET=your_webhook_secret

# Database
DATABASE_URL=postgresql://user:password@localhost:5432/code_review_db

# LLM
OPENAI_API_KEY=sk-...
# OR
ANTHROPIC_API_KEY=sk-ant-...

# App
PORT=8000
```

### 4. Set up the database

```bash
# Create the database
psql -U postgres -c "CREATE DATABASE code_review_db;"

# Run migrations
python -c "from app.database import Base, engine; Base.metadata.create_all(engine)"
```

### 5. Create a GitHub App

1. Go to **GitHub → Settings → Developer Settings → GitHub Apps → New GitHub App**
2. Set the Webhook URL to `https://YOUR_NGROK_URL/webhook`
3. Subscribe to events: **Pull requests** (opened, synchronize, reopened)
4. Generate and download the **Private Key** (.pem file) → save as `private-key.pem`
5. Install the App on your test repository

### 6. Start ngrok (for local development)

```bash
ngrok http 8000
# Copy the https URL → paste into your GitHub App webhook settings
```

### 7. Run the server

```bash
uvicorn app.main:app --reload --port 8000
```

### 8. Test the pipeline

```bash
python tests/test_pipeline.py
```

Open a Pull Request on your test repository — the bot should post inline comments within 30–60 seconds.

---

## 🔐 Security Agent — Sample Output

The Security Agent detects OWASP Top 10 vulnerabilities and outputs structured JSON:

**Input code (vulnerable):**
```python
def get_user(user_id):
    query = f"SELECT * FROM users WHERE id = {user_id}"
    cursor.execute(query)
    return cursor.fetchall()
```

**Agent output:**
```json
[
  {
    "file": "app/views.py",
    "line_start": 2,
    "line_end": 2,
    "severity": "CRITICAL",
    "type": "SQL_INJECTION",
    "description": "User input directly concatenated into SQL query via f-string. Attacker can inject arbitrary SQL by sending input like: 1 OR 1=1",
    "suggested_fix": "Use parameterized queries: cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))",
    "confidence": "HIGH",
    "owasp_category": "A03:2021 Injection"
  }
]
```

**GitHub inline comment (Markdown rendered):**

> ### 🔴 CRITICAL — SQL Injection Risk
> **File:** `app/views.py` · **Line:** 42
>
> User input is directly concatenated into a SQL query via f-string. An attacker can send `1 OR 1=1` to extract all records.
>
> **Suggested Fix:**
> ```python
> # Instead of:
> query = f"SELECT * FROM users WHERE id = {user_id}"
>
> # Use parameterized queries:
> cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
> ```
> *OWASP A03:2021 — Injection*

---

## ⚡ Performance Agent — Sample Output

**Detected pattern — N+1 query:**
```python
def get_posts_with_authors(post_ids):
    posts = []
    for post_id in post_ids:              # N iterations
        post = db.query(Post).get(post_id)
        author = db.query(User).get(post.author_id)  # N extra queries!
        posts.append({...})
    return posts
```

**Agent finding:**
```json
{
  "severity": "HIGH",
  "type": "N_PLUS_ONE_QUERY",
  "description": "Database query inside a for-loop causes N+1 queries. For 1000 posts, this makes 2001 DB calls instead of 2.",
  "suggested_fix": "Use select_related or a JOIN: posts = db.query(Post).options(joinedload(Post.author)).filter(Post.id.in_(post_ids)).all()"
}
```

---

## 🧠 LangGraph Orchestrator

The orchestrator runs all 3 agents **in parallel** using LangGraph's `Send()` API:

```
State: { pr_id, chunks, security_findings, perf_findings, style_findings, final_report }

                    ┌─── security_node ───┐
chunk ──► router ──►├─── performance_node ─┼──► merge ──► deduplicate ──► prioritize ──► post_comments
                    └─── style_node ───────┘
```

**Deduplication logic:** If two agents flag the same `(file, line_start, issue_type)`, only the highest-severity finding is kept.

**Priority order:** `CRITICAL → HIGH → MEDIUM → LOW → INFO`

---

## 📊 Dashboard

The dashboard shows team-level quality trends at `/dashboard`:

- **Findings by severity** (pie chart)
- **Findings by type** (bar chart: Security / Performance / Style)
- **Issues per PR over time** (line chart — shows if the team is improving)
- **Top offending files** (table)

---

## 🔄 Iterative Review

When a developer pushes a **fix commit** to an existing PR:

1. The `synchronize` webhook event fires
2. The bot identifies **only the files that changed** since the last review
3. Only those files are re-parsed and re-analyzed
4. New comments are posted; resolved issues are not re-raised

This means the bot acts as a **collaborative teammate**, not a spammer.

---

## 👥 Team

| Member | Role | Responsibility |
|---|---|---|
| Member 1 | Team Lead / Orchestrator | Project doc, repo setup, end-to-end testing, demo lead |
| Member 2 | GitHub & Webhooks | GitHub App, webhook handler, PR diff fetching |
| Member 3 | FastAPI Backend | Server, PostgreSQL, API endpoints, background tasks |
| Member 4 | Code Parser | tree-sitter AST chunking, token reduction |
| Member 5 | Security AI Agent | OWASP vulnerability detection, prompt engineering |
| Member 6 | Performance AI Agent | N+1 query, complexity, blocking call detection |
| Member 7 | Style Agent + RAG | PEP8 style review, RAG knowledge base pipeline |
| Member 8 | LangGraph Orchestrator | State machine, parallel execution, deduplication |
| Member 9 | UI / Dashboard | GitHub inline comments, quality trend dashboard |

---

## 🧪 Running Tests

```bash
# Run all tests
python -m pytest tests/ -v

# Run only security agent tests
python -m pytest tests/test_security_agent.py -v

# Run the full pipeline integration test
python tests/test_pipeline.py
```

---

## 📋 Requirements

```
fastapi==0.104.1
uvicorn==0.24.0
sqlalchemy==2.0.23
psycopg2-binary==2.9.9
pydantic==2.5.0
langchain==0.0.340
langgraph==0.0.26
openai==1.3.7
anthropic==0.7.7
tree-sitter==0.20.4
tree-sitter-python==0.20.4
chromadb==0.4.18
python-dotenv==1.0.0
requests==2.31.0
PyGithub==2.1.1
pytest==7.4.3
```

---

## 🛣 Roadmap

- [ ] JavaScript / TypeScript support via tree-sitter-javascript
- [ ] Java support via tree-sitter-java
- [ ] GitLab Merge Request integration
- [ ] Slack / Discord notifications on CRITICAL findings
- [ ] Bandit static analysis as a pre-filter (reduce LLM cost)
- [ ] Developer feedback loop — thumbs up/down on findings to improve accuracy
- [ ] Self-hosted LLM option (Ollama + CodeLlama) for air-gapped environments

---

## ❓ FAQ

**Q: How does the bot avoid false positives?**
A: We use few-shot prompting with concrete examples, a confidence scoring system, and RAG-retrieved coding guidelines to give the LLM precise context. Findings below a confidence threshold are filtered or flagged as informational only.

**Q: How much does each PR analysis cost?**
A: With GPT-4o-mini and AST chunking, a typical PR (5–10 changed functions) costs approximately $0.002–$0.01 in API credits — well under a cent for most PRs.

**Q: What happens if the LLM API is down?**
A: Each agent has retry logic with exponential backoff. If all retries fail, the agent returns an empty findings list and the pipeline continues without crashing. The PR is marked as `partially_analyzed` in the database.

**Q: Can it review code it didn't write?**
A: Yes. The bot analyzes any Python code — open-source libraries, legacy codebases, third-party integrations. It does not need to understand the project's business logic to detect security and performance patterns.

**Q: Currently supports Python only?**
A: Yes, for the MVP. tree-sitter supports 100+ languages, so adding JavaScript or Java is a planned extension that requires adding the relevant grammar and updating the agent prompts.

---

## 📄 License

This project was built as an academic portfolio project at CVRGU as part of the AI Training programme.

---

<div align="center">

**Built with 🤖 LangGraph · 🌳 tree-sitter · ⚡ FastAPI · 🐙 GitHub Apps**

*Saving senior developers 5–10 hours per week, one PR at a time.*

</div>
