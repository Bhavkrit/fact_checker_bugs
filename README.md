# 🔍 Fact Checker — Agentic AI Fact-Checking CLI

An agentic AI pipeline that takes a plain-text claim, searches for evidence, and returns a credibility score from 0–100 with a justification.

## 🧭 Order of solving bugs

This is the preferred order to solve the issues, as it keeps the fixes incremental and easier to validate step by step.

1. Issue 1
2. Issue 2
3. Issue 3
4. Issue 4
5. Issue 5
6. Issue 6

---

## ✨ What it does

```text
$ poetry run python -m fact_checker_bugs.cli check "The Great Wall of China is visible from space."

╭──────────────────────────────────────────────────────────────╮
│ Evaluating: The Great Wall of China is visible from space.   │
╰──────────────────────────────────────────────────────────────╯

⠙ Agent is researching live data...

🟡 Credibility Score: 35/100

╭─ Justification ───────────────────────────────────────────────╮
│ Multiple scientific sources, including NASA astronaut reports │
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
````

---

## 🛠️ Prerequisites

Before setting up the project, make sure you have the following installed:

| Tool   | Version            | Download                                                                                     |
| ------ | ------------------ | -------------------------------------------------------------------------------------------- |
| Python | >= 3.14            | [https://www.python.org/downloads/](https://www.python.org/downloads/)                       |
| Poetry | >= 2.0.0           | [https://python-poetry.org/docs/#installation](https://python-poetry.org/docs/#installation) |
| Git    | Any recent version | [https://git-scm.com/downloads](https://git-scm.com/downloads)                               |

### Verify your installations

```bash
python --version
poetry --version
git --version
```

---

## 🚀 Setup Instructions

### Step 1 — Clone the repository

```bash
git clone <repository-url>
cd fact_checker_bugs
```

### Step 2 — Install dependencies

```bash
poetry install
```

### Step 3 — Configure environment variables

Copy the example file:

```bash
cp .env.example .env
```

On Windows PowerShell:

```powershell
Copy-Item .env.example .env
```

Fill in your keys in `.env`:

```dotenv
GEMINI_API_KEY_1=your_key_here
GEMINI_API_KEY_2=optional_second_key
TAVILY_API_KEY=your_tavily_key
```

> Do not commit `.env` to version control.

### Step 4 — Run the CLI

```bash
poetry run python -m fact_checker_bugs.cli check "Your claim goes here"
```

Example:

```bash
poetry run python -m fact_checker_bugs.cli check "The James Webb Space Telescope was launched in 2021."
```

---

## 📁 Project Structure

```text
fact_checker_bugs/
├── .env.example
├── .gitignore
├── pyproject.toml
├── poetry.lock
├── README.md
├── src/
│   └── fact_checker_bugs/
│       ├── __init__.py
│       ├── cli.py
│       ├── graph.py
│       ├── state.py
│       ├── nodes/
│       │   ├── __init__.py
│       │   ├── cross_referencer.py
│       │   ├── query_formulator.py
│       │   ├── retriever.py
│       │   └── scorer.py
│       └── utils/
│           ├── __init__.py
│           └── llm_utils.py
└── tests/
    └── __init__.py
```

---

## ❓ Troubleshooting

### `No Gemini API keys found in environment`

Check that your `.env` file exists and contains valid keys.

### `429 Too Many Requests`

Wait a minute and try again, or add more Gemini keys to rotate between them.

### `Tavily search failed`

Verify that `TAVILY_API_KEY` is set correctly in `.env`.

---

## 🧰 Tech Stack

* LangGraph
* Google Gemini
* Tavily Search
* Typer
* Rich
* Poetry