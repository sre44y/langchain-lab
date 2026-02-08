# langchain-lab

A minimal LangChain + OpenAI starter project in Python.

## What it does

`main.py`:
- Loads environment variables from `.env`
- Creates a `ChatOpenAI` client (`gpt-4o-mini`, `temperature=0`)
- Sends a short prompt and prints the model response

## Prerequisites

- Python 3.10+ (recommended)
- An OpenAI API key

## Setup

1. Create and activate a virtual environment:

```powershell
python -m venv .venv
.venv\Scripts\activate
```

2. Install dependencies:

```powershell
pip install langchain-openai python-dotenv
```

3. Create or update `.env`:

```env
OPENAI_API_KEY=your_api_key_here
```

## Run

```powershell
python main.py
```

## Project structure

```text
.
|-- main.py
|-- .env
|-- .gitignore
`-- README.md
```
