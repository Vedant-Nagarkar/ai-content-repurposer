# AI Content Repurposer

A Gradio app that takes any long-form text and repurposes it into three formats using different prompt engineering techniques.

## What It Does

Paste any article, blog post, or notes — select an output format — get repurposed content instantly.

| Format | Prompt Technique |
|---|---|
| LinkedIn Post | Role Prompting |
| Twitter Thread | Few-Shot Prompting |
| Executive Summary | Chain-of-Thought Prompting |

## Project Structure

```
ai-content-repurposer/
├── src/
│   ├── logger.py       # Centralized logging
│   ├── data.py         # Input validation and cleaning
│   ├── features.py     # Prompt construction
│   ├── model.py        # Groq API calls
│   ├── evaluate.py     # Output quality checks
│   └── predict.py      # End-to-end pipeline
├── tests/              # Pytest test suite
├── data/               # Sample input texts
├── logs/               # Auto-generated logs
├── app.py              # Gradio UI
├── config.py           # All constants and settings
└── .env                # API keys (never committed)
```

## Setup

**1. Clone the repo**
```bash
git clone https://github.com/Vedant-Nagarkar/ai-content-repurposer.git
cd ai-content-repurposer
```

**2. Create and activate conda environment**
```bash
conda create -n content-repurposer python=3.11 -y
conda activate content-repurposer
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Set up environment variables**
```bash
cp .env.example .env
```
Open `.env` and add your Groq API key:

Get a free Groq API key at [console.groq.com](https://console.groq.com)

## Run

```bash
python app.py
```

Then open `http://127.0.0.1:7860` in your browser.

## Test

```bash
pytest tests/ -v
```

## Model

Uses `llama-3.1-8b-instant` via Groq API — fast, free, and accurate for text generation tasks.

## Author

Vedant Nagarkar — [GitHub](https://github.com/Vedant-Nagarkar) · [LinkedIn](https://www.linkedin.com/in/vedant-nagarkar/)