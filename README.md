# AI Content Repurposer

A Gradio app that repurposes any long-form text into three formats using different prompt engineering techniques.

## Output Formats
- **LinkedIn Post** — Role Prompting
- **Twitter Thread** — Few-Shot Prompting
- **Executive Summary** — Chain-of-Thought Prompting

## Setup

```bash
conda activate content-repurposer
pip install -r requirements.txt
```

## Run

```bash
python app.py
```

## Project Structure
ai-content-repurposer/
├── src/
│   ├── logger.py        # Centralized logging
│   ├── data.py          # Input validation and cleaning
│   ├── features.py      # Prompt construction
│   ├── model.py         # LLM API calls
│   ├── evaluate.py      # Output quality checks
│   └── predict.py       # End-to-end pipeline
├── tests/               # Pytest smoke tests
├── data/                # Sample input texts
├── logs/                # Auto-generated logs
├── app.py               # Gradio UI
├── config.py            # All constants and settings
└── .env                 # API keys (never committed)