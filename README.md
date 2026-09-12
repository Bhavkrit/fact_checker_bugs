# 🔍 Fact Checker — Agentic AI Fact-Checking CLI

An agentic AI pipeline that takes any plain-text claim, autonomously searches the web for evidence, and returns a **credibility score (0–100)** with a detailed justification — powered by **LangGraph**, **Google Gemini**, and **Tavily Search**.

---

## ✨ What it does

```
$ poetry run fact-checker check "The Great Wall of China is visible from space."

╭──────────────────────────────────────────────────────────────╮
│ Evaluating: The Great Wall of China is visible from space.   │
╰──────────────────────────────────────────────────────────────╯
⠙ Agent is researching live data...

🟡 Credibility Score: 35/100

╭─ Justification ───────────────────────────────────────────────╮
│ Multiple scientific sources, including NASA astronaut reports  │
│ and optical physics analysis, confirm that the wall is far too │
│ narrow (~10 m) to be seen by the naked eye from low Earth      │
│ orbit (~400 km). This is a well-documented myth...            │
╰───────────────────────────────────────────────────────────────╯

               Sources Consulted
┌──────────────────────────┬──────────────────────────────┐
│ Title                    │ URL                          │
├──────────────────────────┼──────────────────────────────┤
│ NASA Earth Observatory   │ https://earthobservatory...  │
│ Scientific American      │ https://scientificamerican.. │
└──────────────────────────┴──────────────────────────────┘
```

---

## 🛠️ Prerequisites

Before setting up the project, make sure you have the following installed:

| Tool | Version | Download |
|------|---------|----------|
| **Python** | `>= 3.14` | [python.org](https://www.python.org/downloads/) |
| **Poetry** | `>= 2.0.0` | [python-poetry.org](https://python-poetry.org/docs/#installation) |
| **Git** | Any recent version | [git-scm.com](https://git-scm.com/downloads) |

### Verify your installations

```bash
python --version      # Should print Python 3.14.x or higher
poetry --version      # Should print Poetry 2.x.x
git --version         # Should print git version x.x.x
```

---

## 🚀 Setup Instructions

Follow these steps **in order** to get the project running on your machine.

### Step 1 — Clone the repository

```bash
git clone <repository-url>
cd fact_checker_project
```

> Replace `<repository-url>` with the actual GitHub URL shared with you.

---

### Step 2 — Install dependencies

Poetry automatically creates a virtual environment and installs all locked dependencies:

```bash
poetry install
```

You should see output like:
```
Creating virtualenv fact-checker-project-... in ...
Installing dependencies from lock file
...
Installing the current project: fact-checker-project (0.1.0)
```

---

### Step 3 — Get your API Keys

You need **two** sets of API keys:

#### 🔑 Google Gemini API Key (Required — get at least 1, up to 4)

1. Go to [Google AI Studio](https://aistudio.google.com/)
2. Sign in with your Google account
3. Click **"Get API Key"** → **"Create API key"**
4. Copy the key (it looks like `AIzaSy...`)

> 💡 **Pro tip:** Create 2–3 keys from different Google accounts to avoid hitting the free-tier rate limit (60 requests/minute per key).

#### 🔑 Tavily API Key (Required — 1 key is enough)

1. Go to [app.tavily.com](https://app.tavily.com/)
2. Sign up for a free account
3. Your API key is on the dashboard (it looks like `tvly-...`)

> The free tier gives you **1,000 searches/month** — more than enough for testing.

---

### Step 4 — Configure environment variables

Copy the example `.env` file:

```bash
# On macOS / Linux
cp .env.example .env

# On Windows (PowerShell)
Copy-Item .env.example .env
```

Now open `.env` in any text editor and fill in your keys:

```dotenv
# ── Google Gemini API Keys (at least GEMINI_API_KEY_1 is required) ──
GEMINI_API_KEY_1=AIzaSy_your_first_key_here
GEMINI_API_KEY_2=AIzaSy_your_second_key_here    # optional but recommended
GEMINI_API_KEY_3=AIzaSy_your_third_key_here     # optional

# ── Tavily Search API Key (required) ──
TAVILY_API_KEY=tvly-your_tavily_key_here

# ── Optional: LangSmith tracing (for debugging) ──
# LANGCHAIN_TRACING_V2=true
# LANGCHAIN_API_KEY=your_langsmith_key_here
# LANGCHAIN_PROJECT=fact_checker_project
```

> ⚠️ **Never commit `.env` to Git.** It is already listed in `.gitignore`.

---

### Step 5 — Run the fact-checker

```bash
poetry run fact-checker check "Your claim goes here"
```

#### Examples to try

```bash
# Science claims
poetry run fact-checker check "Humans only use 10% of their brain."

# Historical claims
poetry run fact-checker check "The Great Wall of China is visible from space."

# Current events
poetry run fact-checker check "Electric vehicles produce zero emissions."

# Conspiracy theories
poetry run fact-checker check "The Moon landing was faked."
```

---

## 🎯 Understanding the Output

| Score Range | Colour | Meaning |
|-------------|--------|---------|
| **71 – 100** | 🟢 Green | Claim is well-supported by evidence |
| **40 – 70** | 🟡 Yellow | Evidence is mixed or inconclusive |
| **0 – 39** | 🔴 Red | Claim is contradicted by evidence or unsupported |

---

## ❓ Troubleshooting

### `No Gemini API keys found in environment`

Your `.env` file is either missing or the keys have typos. Double-check:
```bash
# Make sure .env exists
ls -la .env        # macOS/Linux
dir .env           # Windows

# Preview the file (make sure keys are filled in, not placeholder text)
cat .env           # macOS/Linux
type .env          # Windows
```

### `429 Too Many Requests` (rate limit error)

The free-tier Gemini API has a rate limit of 60 requests per minute per key. Solutions:
- **Wait 1 minute** and try again.
- Add 2–3 Gemini API keys (`GEMINI_API_KEY_2`, `GEMINI_API_KEY_3`) — the agent rotates between them automatically.

### `Tavily search failed`

- Check that `TAVILY_API_KEY` is set correctly in `.env`.
- Verify your Tavily account has remaining search credits at [app.tavily.com](https://app.tavily.com/).

### `python --version` shows Python < 3.14

This project requires Python 3.14 or higher. Download the latest version from [python.org](https://www.python.org/downloads/) and re-run `poetry install`.

### Poetry command not found

Install Poetry by following the [official instructions](https://python-poetry.org/docs/#installation):

```bash
# macOS / Linux / WSL
curl -sSL https://install.python-poetry.org | python3 -

# Windows (PowerShell)
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```

After installing, restart your terminal.

---

## 📁 Project Structure

```
fact_checker_project/
├── .env                      # Your secrets (never commit this!)
├── .env.example              # Template for required environment variables
├── pyproject.toml            # Project metadata and dependencies
├── poetry.lock               # Locked dependency versions
│
├── src/
│   └── fact_checker/
│       ├── cli.py            # CLI entry point (`fact-checker check`)
│       ├── graph.py          # LangGraph agent pipeline
│       ├── state.py          # Shared data schema
│       └── nodes/
│           ├── query_formulator.py  # Generates search queries (LLM)
│           ├── retriever.py         # Searches the web (Tavily)
│           ├── cross_referencer.py  # Deduplicates results
│           └── scorer.py            # Scores the claim (LLM)
│
└── tests/                    # Test suite
```

---

## 🧰 Tech Stack

| Component | Technology |
|-----------|-----------|
| Agent Framework | [LangGraph](https://github.com/langchain-ai/langgraph) |
| LLM | [Google Gemini](https://aistudio.google.com/) via LangChain |
| Web Search | [Tavily Search API](https://tavily.com/) |
| CLI | [Typer](https://typer.tiangolo.com/) |
| Terminal UI | [Rich](https://rich.readthedocs.io/) |
| Package Manager | [Poetry](https://python-poetry.org/) |
