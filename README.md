# MediShield Safety Engine

MediShield Safety Engine is an AI-powered content moderation and safety analysis project.
It is designed to evaluate datasets, detect unsafe content, and apply rule-based and model-driven guardrails.

## Features

- AI-based safety and moderation checks
- Dataset evaluation and metrics generation
- Offline action and rule engine
- Secure API usage with environment variables
- Clean and modular Python design

## Project Structure

medishield-safety-engine/
│
├── analysis.py               # Core analysis logic
├── evaluate_dataset.py       # Dataset evaluation script
├── metrics.py                # Metrics and scoring utilities
├── offline_action_engine.py  # Rule-based safety engine
├── config.py                 # Configuration (no hardcoded secrets)
├── requirements.txt          # Python dependencies
├── .gitignore                # Ignored files and secrets
└── README.md                 # Project documentation

## Setup Instructions

1. Clone the repository:
   git clone https://github.com/ishwariwakchaure5/medishield-safety-engine.git
   cd medishield-safety-engine

2. Create a virtual environment:
   python -m venv .venv
   source .venv/bin/activate   (macOS / Linux)

3. Install dependencies:
   pip install -r requirements.txt

4. Create a .env file:
   OPENAI_API_KEY=your_api_key_here

## Usage

Run dataset evaluation:
   python evaluate_dataset.py

Run analysis module:
   python analysis.py

## Security Notes

- API keys are stored in a .env file and are never committed
- .env, cache files, and generated data are ignored using .gitignore

## Author

Ishwari Wakchaure

## License

This project is for educational and research purposes.
