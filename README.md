<div align="center">

<!-- Animated wave banner -->
<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:0D1117,50:00D9FF,100:7B2FBE&height=200&section=header&text=AI%20Code%20Review%20Agent&fontSize=50&fontColor=ffffff&fontAlignY=38&desc=LangGraph%20%7C%20Tree-sitter%20AST%20%7C%20FastAPI%20%7C%20GPT-4o-mini&descAlignY=58&descSize=18&animation=fadeIn" />

<!-- Animated typing SVG -->
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=24&pause=1000&color=00D9FF&center=true&vCenter=true&repeat=true&width=750&height=60&lines=🤖+Automated+Code+Review+via+GitHub+Webhooks;🌳+Tree-sitter+AST+%7C+~95%25+Token+Reduction;⚡+LangGraph+Parallel+Multi-Agent+Pipeline;🔐+Security+%7C+Performance+%7C+Style+Analysis;🚀+Production-Ready+%7C+Docker+%7C+35+Tests+Passing" alt="Typing SVG" />

<br/>

<!-- Animated badges -->
<a href="https://python.org"><img src="https://img.shields.io/badge/Python-3.11%2B-3776AB?style=for-the-badge&logo=python&logoColor=white&labelColor=0D1117" /></a>
<a href="https://fastapi.tiangolo.com"><img src="https://img.shields.io/badge/FastAPI-0.111-009688?style=for-the-badge&logo=fastapi&logoColor=white&labelColor=0D1117" /></a>
<a href="https://langchain-ai.github.io/langgraph/"><img src="https://img.shields.io/badge/LangGraph-1.1.3-FF6B6B?style=for-the-badge&logo=chainlink&logoColor=white&labelColor=0D1117" /></a>
<a href="https://openai.com"><img src="https://img.shields.io/badge/OpenAI-GPT--4o--mini-412991?style=for-the-badge&logo=openai&logoColor=white&labelColor=0D1117" /></a>

<br/><br/>

<a href="https://docker.com"><img src="https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white&labelColor=0D1117" /></a>
<a href="https://pytest.org"><img src="https://img.shields.io/badge/Tests-35%20Passing-00C853?style=for-the-badge&logo=pytest&logoColor=white&labelColor=0D1117" /></a>
<img src="https://img.shields.io/badge/Coverage-95%25-00C853?style=for-the-badge&logo=codecov&logoColor=white&labelColor=0D1117" />
<img src="https://img.shields.io/badge/License-MIT-F7DF1E?style=for-the-badge&logo=opensourceinitiative&logoColor=white&labelColor=0D1117" />

<br/><br/>

<!-- Animated description -->
<p>
<img src="https://readme-typing-svg.demolab.com?font=Roboto&size=16&pause=2000&color=AAAAAA&center=true&vCenter=true&width=750&lines=A+production-ready+AI+agent+that+intercepts+GitHub+Pull+Requests%2C;parses+code+with+Tree-sitter+AST%2C+and+runs+a+parallel+LangGraph;multi-agent+pipeline+to+detect+security+flaws%2C+performance+issues%2C;and+style+violations+—+then+posts+findings+as+inline+PR+comments." alt="Description" />
</p>

<br/>

<!-- Navigation -->
[🚀 Quick Start](#-quick-start) • [🏗️ Architecture](#️-architecture) • [⚙️ Installation](#️-installation) • [🐳 Docker](#-docker) • [🧪 Tests](#-running-tests) • [📡 API](#-api-endpoints)

</div>

<!-- Animated divider -->
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">

## ✨ Features

<table>
<tr>
<td width="50%">

### 🔐 Security Analysis
- SQL / NoSQL injection detection
- Hardcoded secrets & API keys
- Command injection (`shell=True`)
- Insecure deserialization (`pickle`)
- Path traversal vulnerabilities
- Full **OWASP Top-10** coverage

</td>
<td width="50%">

### ⚡ Performance Analysis
- N+1 query pattern detection
- O(n²) loop identification
- Blocking I/O in async functions
- Missing bulk operations
- Repeated expensive calls
- Caching opportunity hints

</td>
</tr>
<tr>
<td width="50%">

### 🎨 Style Analysis
- PEP 8 violation detection
- Missing docstrings & type hints
- Magic numbers & unclear names
- Functions > 20 lines undocumented
- Import organization issues

</td>
<td width="50%">

### 🧠 Smart Architecture
- **~95% token reduction** via AST chunking
- Parallel agent execution (LangGraph)
- Deduplication + severity sorting
- Rate-limited LLM calls (Semaphore)
- Batched GitHub inline PR comments

</td>
</tr>
</table>

<!-- Animated divider -->
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        GitHub PR Event                          │
└──────────────────────────────┬──────────────────────────────────┘
                               │  POST /webhook
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│                    FastAPI  (main.py)                           │
│  ① HMAC-SHA256 signature verification                           │
│  ② Filter: opened / synchronize / reopened only                 │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                    ┌──────────▼──────────┐
                    │   github_client.py  │
                    │  • Fetch raw diff   │
                    │  • Fetch .py files  │
                    └──────────┬──────────┘
                               │
                    ┌──────────▼──────────┐
                    │     parser.py       │  ◄── ~95% Token Reduction
                    │  Tree-sitter AST    │  500 lines → 30 lines
                    │  Semantic Chunking  │  (only changed functions)
                    └──────────┬──────────┘
                               │
          ┌────────────────────▼────────────────────┐
          │           LangGraph Pipeline             │
          │                                          │
          │         ┌─── Orchestrator ───┐           │
          │         │                   │           │
          │    ┌────▼────┐  ┌───────────▼──┐  ┌────▼─────┐
          │    │Security │  │ Performance  │  │  Style   │
          │    │ Agent   │  │   Agent      │  │  Agent   │
          │    │OWASP Top│  │ N+1, O(n²)  │  │ PEP 8   │
          │    └────┬────┘  └──────┬───────┘  └────┬─────┘
          │         └──────────────┼────────────────┘
          │                        │
          │              ┌─────────▼─────────┐
          │              │    Synthesizer     │
          │              │  Dedup + Sort      │
          │              │  High→Medium→Low   │
          │              └─────────┬─────────┘
          └────────────────────────┼─────────────────┘
                                   │
                    ┌──────────────▼──────────────┐
                    │      github_client.py        │
                    │  Post inline PR comments     │
                    │  (single batched review)     │
                    └─────────────────────────────┘
```

### 💡 Why ~95% Token Reduction?

| Approach | File Size | Tokens Sent | Cost |
|:---|:---:|:---:|:---:|
| Raw diff approach | 500 lines | ~5,000 tokens | 💸 Expensive |
| **AST Semantic Chunking** | 500 lines | **~300 tokens** | ✅ **94% cheaper** |

> Tree-sitter builds a full syntax tree and extracts **only** the `function_definition` / `class_definition` nodes that overlap with changed lines. The LLM receives complete, syntactically valid code units — not truncated diff hunks — which also **improves review quality**.

<!-- Animated divider -->
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">

## 🛠️ Tech Stack

<div align="center">

<!-- Animated skill icons -->
<img src="https://skillicons.dev/icons?i=python,fastapi,docker,git,github,vscode,linux&theme=dark&perline=7" />

<br/><br/>

| Layer | Technology |
|:---|:---|
| 🌐 Web Framework | [FastAPI](https://fastapi.tiangolo.com) + Uvicorn |
| 🤖 AI Orchestration | [LangGraph 1.x](https://langchain-ai.github.io/langgraph/) |
| 🧠 LLM | [OpenAI GPT-4o-mini](https://openai.com) via LangChain |
| 🌳 AST Parsing | [Tree-sitter](https://tree-sitter.github.io) + tree-sitter-python |
| 🐙 GitHub Integration | [PyGithub](https://pygithub.readthedocs.io) |
| 🔗 HTTP Client | [httpx](https://www.python-httpx.org) |
| ⚙️ Config | [python-dotenv](https://pypi.org/project/python-dotenv/) |
| 🧪 Testing | [pytest](https://pytest.org) + pytest-asyncio |
| 🐳 Containerisation | Docker + docker-compose |

</div>

<!-- Animated divider -->
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">

## 📁 Project Structure

```
AI-powered-Code-Review-Bug-Detection-Agent/
│
├── 📁 src/                        ← Application source code
│   ├── 🚀 main.py                 FastAPI entrypoint + webhook handler
│   ├── 🤖 agents.py               LangGraph state machine + agent nodes
│   ├── 🌳 parser.py               Tree-sitter AST semantic chunker
│   ├── 🐙 github_client.py        GitHub API: fetch PR data, post comments
│   └── ⚙️  config.py               Env-var loading via python-dotenv
│
├── 📁 tests/                      ← All test files
│   ├── 🧪 test_parser.py          Diff parsing, AST, token reduction
│   ├── 🧪 test_agents.py          LLM mocking, agents, synthesizer
│   └── 🧪 test_webhook.py         FastAPI endpoint integration tests
│
├── 📁 docker/                     ← Container configuration
│   ├── 🐳 Dockerfile
│   └── 🐳 docker-compose.yml
│
├── 📦 requirements.txt
├── 🔧 pytest.ini
├── 🔑 .env.example
└── 🚫 .gitignore
```

<!-- Animated divider -->
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">

## ⚙️ Installation

### Prerequisites

| Tool | Version | Download |
|:---|:---:|:---:|
| 🐍 Python | 3.11+ | [python.org](https://python.org/downloads) |
| 🔧 Git | Any | [git-scm.com](https://git-scm.com/downloads) |
| 🌐 ngrok *(dev only)* | Any | [ngrok.com/download](https://ngrok.com/download) |
| 🐳 Docker *(optional)* | Any | [docker.com](https://docker.com/get-started) |

<!-- Animated divider -->
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">

## 🚀 Quick Start

### Step 1 — Clone the repository

```bash
git clone https://github.com/AI-Code-Review-Team/AI-powered-Code-Review-Bug-Detection-Agent.git
cd AI-powered-Code-Review-Bug-Detection-Agent
```

### Step 2 — Create a virtual environment

```bash
# 🪟 Windows
python -m venv venv
venv\Scripts\activate

# 🍎 macOS / 🐧 Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3 — Install dependencies

```bash
pip install -r requirements.txt
```

### Step 4 — Configure environment variables

```bash
# 🪟 Windows
copy .env.example .env

# 🍎 macOS / 🐧 Linux
cp .env.example .env
```

Now open `.env` and fill in your credentials:

```env
# GitHub Personal Access Token (needs: repo + pull_requests scopes)
GITHUB_TOKEN=ghp_your_github_token_here

# Secret you set when registering the GitHub webhook
GITHUB_WEBHOOK_SECRET=your_webhook_secret_here

# OpenAI API key — get one at https://platform.openai.com/api-keys
OPENAI_API_KEY=sk-your_openai_key_here

# Optional: swap to gpt-4o for higher accuracy (default: gpt-4o-mini)
LLM_MODEL=gpt-4o-mini
```

> 🔑 **Get your keys:**
> - GitHub Token → [github.com/settings/tokens](https://github.com/settings/tokens) → Classic token → `repo` scope
> - OpenAI Key → [platform.openai.com/api-keys](https://platform.openai.com/api-keys)

### Step 5 — Run the server

```bash
uvicorn src.main:app --reload --port 8000
```

```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
```

Visit **http://localhost:8000/health** to confirm it's running ✅

### Step 6 — Expose to GitHub via ngrok

```bash
ngrok http 8000
```

Copy the HTTPS URL shown, e.g. `https://abc123.ngrok-free.app`

### Step 7 — Register the GitHub Webhook

1. Go to your GitHub repo → **Settings** → **Webhooks** → **Add webhook**
2. Fill in:

| Field | Value |
|:---|:---|
| Payload URL | `https://abc123.ngrok-free.app/webhook` |
| Content type | `application/json` |
| Secret | Same value as `GITHUB_WEBHOOK_SECRET` in your `.env` |
| Events | ✅ **Pull requests** only |

3. Click **Add webhook** — GitHub sends a ping → you'll see a ✅ green tick

### Step 8 — Test it!

Open a Pull Request in your repo — the agent will automatically:
1. 📥 Receive the webhook event
2. 📂 Fetch the diff and changed files
3. 🌳 Run AST chunking + multi-agent analysis
4. 💬 Post inline comments on your PR 🎉

<!-- Animated divider -->
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">

## 🐳 Docker

```bash
# Clone & configure
git clone https://github.com/AI-Code-Review-Team/AI-powered-Code-Review-Bug-Detection-Agent.git
cd AI-powered-Code-Review-Bug-Detection-Agent
cp .env.example .env   # fill in your keys

# Build and run with docker-compose
docker-compose -f docker/docker-compose.yml up --build
```

Or with plain Docker:

```bash
docker build -f docker/Dockerfile -t ai-code-review-agent .
docker run -p 8000:8000 --env-file .env ai-code-review-agent
```

<!-- Animated divider -->
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">

## 🧪 Running Tests

Tests use **mocked LLM and GitHub API calls** — no real credentials needed:

```bash
pytest -v
```

```
tests/test_agents.py::test_call_llm_parses_json_array          PASSED
tests/test_agents.py::test_security_agent_returns_findings     PASSED
tests/test_agents.py::test_synthesizer_sorts_by_severity       PASSED
tests/test_agents.py::test_full_graph_returns_final_findings   PASSED
tests/test_parser.py::test_parse_diff_hunks_returns_correct_file PASSED
tests/test_parser.py::test_ast_extracts_function               PASSED
tests/test_parser.py::test_token_reduction_demonstration       PASSED
tests/test_webhook.py::test_webhook_processes_opened_pr        PASSED
...
====================== 35 passed in 3.64s ======================
```

| Test File | What's Covered |
|:---|:---|
| `tests/test_parser.py` | Diff parsing, AST extraction, regex fallback, token reduction |
| `tests/test_agents.py` | LLM mocking, all agent nodes, synthesizer dedup/sort, full graph |
| `tests/test_webhook.py` | Signature validation, event filtering, happy path, error handling |

<!-- Animated divider -->
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">

## 📡 API Endpoints

| Method | Endpoint | Description |
|:---:|:---|:---|
| `POST` | `/webhook` | GitHub PR webhook receiver |
| `GET` | `/health` | Liveness probe — returns server + tree-sitter status |

### Health Check Response

```json
{
  "status": "ok",
  "tree_sitter_available": true
}
```

### Webhook Response (on PR event)

```json
{
  "status": "ok",
  "pr": 42,
  "chunks_analysed": 7,
  "findings_count": 4,
  "findings": [
    {
      "file": "app/views.py",
      "line": 42,
      "severity": "High",
      "issue": "SQL injection via f-string interpolation in query",
      "fix": "Use parameterised queries: db.execute('SELECT * FROM users WHERE name=?', (user,))"
    }
  ]
}
```

<!-- Animated divider -->
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">

## 🔍 How Findings Look on GitHub

```
🔴 [High] SQL injection via f-string interpolation
Suggested fix: Use parameterised queries:
db.execute('SELECT * FROM users WHERE name=?', (user,))
```

```
🟡 [Medium] N+1 query pattern — DB call inside a for-loop
Suggested fix: Use bulk fetch before the loop:
users = User.objects.filter(id__in=user_ids)
```

```
🟢 [Low] Missing docstring on public function `process_payment`
Suggested fix: Add a docstring describing parameters and return value.
```

Findings are always sorted: 🔴 **High** → 🟡 **Medium** → 🟢 **Low**

<!-- Animated divider -->
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">

## 🛡️ Rate Limiting & Safety

| Protection | Implementation |
|:---|:---|
| LLM rate limiting | `asyncio.Semaphore(5)` — max 5 concurrent OpenAI calls |
| GitHub API safety | All findings batched into **one** `create_review()` call |
| Blocking I/O | All GitHub calls run in thread pool via `run_in_executor` |
| Webhook security | HMAC-SHA256 signature verified on every request |

<!-- Animated divider -->
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">

## 🔧 Troubleshooting

<details>
<summary><b>❌ tree-sitter import error</b></summary>

```bash
pip install tree-sitter==0.25.2 tree-sitter-python==0.23.6
```
</details>

<details>
<summary><b>❌ OpenAI AuthenticationError</b></summary>

Make sure your `.env` file has a valid `OPENAI_API_KEY` and is in the project root.
</details>

<details>
<summary><b>❌ Webhook shows "Invalid signature"</b></summary>

Ensure `GITHUB_WEBHOOK_SECRET` in `.env` exactly matches the secret in GitHub's webhook settings.
</details>

<details>
<summary><b>❌ ngrok tunnel not working</b></summary>

```bash
uvicorn src.main:app --port 8000   # terminal 1
ngrok http 8000                    # terminal 2
```
</details>

<!-- Animated footer wave -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:7B2FBE,50:00D9FF,100:0D1117&height=120&section=footer&animation=fadeIn" width="100%"/>

<div align="center">

<!-- Animated contribution snake -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/r4hul-s3thi/r4hul-s3thi/output/github-contribution-grid-snake-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/r4hul-s3thi/r4hul-s3thi/output/github-contribution-grid-snake.svg" />
  <img alt="github-snake" src="https://raw.githubusercontent.com/r4hul-s3thi/r4hul-s3thi/output/github-contribution-grid-snake-dark.svg" />
</picture>

<br/>

<!-- Animated profile views counter -->
<img src="https://komarev.com/ghpvc/?username=r4hul-s3thi&label=Profile+Views&color=00D9FF&style=for-the-badge&labelColor=0D1117" />

<br/><br/>

<!-- Animated footer text -->
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=14&pause=1000&color=666666&center=true&vCenter=true&width=500&lines=Made+with+❤️+by+r4hul-s3thi;If+this+helped+you%2C+drop+a+⭐+star!" alt="Footer" />

<br/>

**Made with ❤️ by [r4hul-s3thi](https://github.com/r4hul-s3thi)**

⭐ **Star this repo if you found it useful!** ⭐

</div>
