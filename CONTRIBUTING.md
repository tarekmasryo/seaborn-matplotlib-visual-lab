# Contributing

This is a portfolio project. Issues and suggestions are welcome.

## Ways to contribute
- Report bugs with steps to reproduce and relevant logs.
- Suggest improvements for UX, performance, or reliability.
- Propose focused PRs for docs, tests, or refactors.
- For security issues, avoid posting sensitive details publicly.

## Dev setup

From the repo root, inside a virtual environment:

```bash
python -m pip install -r requirements.txt
python -m pip install -r requirements-dev.txt
python -m ruff check .
python -m ruff format --check .
python -m pytest -q
python -m streamlit run app.py
```
