# 🧩 Case Study — Seaborn & Matplotlib Visual Lab

## Context
Many visualization projects stay as notebooks: hard to reuse, inconsistent exports, and difficult to validate in CI.

This repo packages a visualization learning workflow into an interactive Streamlit app that:
- builds plots from UI controls,
- shows the generated code,
- exports consistent PNGs (and ZIP galleries),
- and remains testable and maintainable.

---

## Problem
- Learning visualization often requires repetitive boilerplate and copy/paste.
- Notebooks are great for exploration, but weak for sharing a consistent interactive experience.
- Visualization code can break when dependencies change (Seaborn/Streamlit API changes).

---

## Solution
A Streamlit “visual lab” with:
- dataset loading (Seaborn catalog),
- Seaborn builders (high-level API patterns),
- Matplotlib builders (low-level control),
- side-by-side comparison,
- a gallery for exporting outputs.

---

## Key engineering decisions

### 1) CI-friendly entrypoint (safe imports)
The app avoids expensive work at import-time by keeping heavy logic inside functions.
This makes `import app` safe for smoke tests and GitHub Actions.

### 2) Offline resilience
If Seaborn’s dataset catalog is unavailable, the app falls back to a small built-in dataset to keep the UI usable.

### 3) Quality gates
- `ruff` for formatting/linting
- `pytest` smoke tests
- `pre-commit` hooks (optional)
- GitHub Actions to validate PRs

---

## Validation
- Local run: `streamlit run app.py`
- Lint/format: `python -m ruff check . --fix` and `python -m ruff format .`
- Tests: `python -m pytest -q`

---

## Result
A clean, reproducible visualization playground that is:
- interactive (UI-driven),
- explainable (code shown),
- exportable (PNG/ZIP),
- and stable under CI (tests + safe imports).

---

## Next steps (optional)
- Add a small performance budget (cache heavy computations).
- Add a “gallery metadata” export (JSON) for reproducible plot settings.
- Provide a minimal Docker deploy guide (if needed).
