# 🔍 Fact Checker — Agentic AI Fact-Checking CLI

An agentic AI pipeline that takes a plain-text claim, searches for evidence, and returns a credibility score from 0–100 with a justification.

---

## 🐛 Challenge Issues

This repository contains six issues that participants are expected to investigate and resolve.

### Recommended solve order

**Issue 1 → Issue 2 → Issue 3 → Issue 4 → Issue 5 → Issue 6**

### Issue 1 — Some valid search results are being lost

Some search results are dropped when optional metadata is missing. The application should keep usable results even if some fields are absent.

### Issue 2 — Duplicate evidence is being counted

The same source can appear multiple times when its URL differs only by tracking parameters or minor variations.

### Issue 3 — Research evidence disappears between rounds

Sources collected in earlier rounds must remain available as new rounds add more evidence.

### Issue 4 — Research prompts grow unnecessarily

Previous evidence is appended in a way that makes prompts repeatedly larger without adding value.

### Issue 5 — Retrieved content can influence model instructions

Web content should remain evidence, not be treated as trusted instructions to the model.

### Issue 6 — Research does not reliably terminate

The research loop should stop after the intended limit instead of continuing unnecessarily.

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

## 📋 Challenge Guidelines

* Solve the issues in the recommended order where possible.
* Fix the underlying issue rather than applying a workaround for a specific input.
* Do not remove or bypass existing functionality.
* Keep changes focused on the reported issue.
* Add regression tests where appropriate.
* Do not commit API keys or other sensitive information.

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