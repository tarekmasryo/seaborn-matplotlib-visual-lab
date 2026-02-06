# 📊 Seaborn & Matplotlib Visual Lab

[![Streamlit](https://img.shields.io/badge/Powered%20by-Streamlit-FF4B4B)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-Apache%202.0-orange.svg)](LICENSE)

An interactive **Streamlit** lab to learn and compare **Seaborn** and **Matplotlib**. Build plots from UI controls, inspect the generated code, and export clean PNGs (or a ZIP gallery).

---

## 🧪 What this app does

- Load classic **Seaborn demo datasets** in one click (Tips, Penguins, Flights, Iris, Diamonds, Titanic, Car Crashes).
- Build **Seaborn** charts (distribution, relationship, category, heatmaps, pairplots) using simple controls.
- Recreate the same ideas with **Matplotlib** to understand the low-level API.
- Compare **Seaborn vs Matplotlib** side by side.
- Save figures to a **gallery** and export PNGs or a ZIP archive.

**Offline-friendly:** if Seaborn’s online dataset catalog is unavailable, the app falls back to a small built-in dataset to keep the UI usable.

---

## 🧭 App structure

| Tab | Purpose |
|:---|:--------|
| **Overview** | Dataset health check: sample, dtypes, missingness, and a small correlation view. |
| **Seaborn builder** | UI-driven Seaborn plots + auto-updating Python snippet. |
| **Matplotlib builder** | Low-level Matplotlib plots with control over axes, grids, and layout. |
| **Compare** | Same visualization idea shown with Seaborn and Matplotlib. |
| **Gallery** | Saved figures, PNG download, and ZIP export. |

---

## 📚 Data sources

Datasets are pulled from **Seaborn’s built-in catalog**:

- `tips`
- `penguins`
- `flights`
- `iris`
- `diamonds` (sample)
- `titanic`
- `car_crashes`

---

## 📸 Dashboard preview

<p align="center">
  <img src="assets/seaborn-tips-total-bill-hist-sex.png" alt="Seaborn histogram (tips dataset)" />
</p>

<p align="center">
  <img src="assets/seaborn-tips-total-bill-vs-tip-scatter.png" alt="Seaborn scatter (tips dataset)" />
</p>

<p align="center">
  <img src="assets/matplotlib-iris-sepal-length-hist.png" alt="Matplotlib histogram (iris dataset)" />
</p>

<p align="center">
  <img src="assets/compare-hist-kde-tips.png" alt="Compare: Seaborn vs Matplotlib histogram + KDE (tips)" />
</p>

---

## 🚀 Quick start (local)

### Option A — Windows (PowerShell)

```bash
git clone https://github.com/tarekmasryo/seaborn-matplotlib-visual-lab.git
cd seaborn-matplotlib-visual-lab

py -3.11 -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1

python -m pip install -U pip
python -m pip install -r requirements.txt
python -m pip install -r requirements-dev.txt

streamlit run app.py
```

Open: http://localhost:8501

### Option B — Linux / macOS

```bash
git clone https://github.com/tarekmasryo/seaborn-matplotlib-visual-lab.git
cd seaborn-matplotlib-visual-lab

python3 -m venv .venv
source .venv/bin/activate

python -m pip install -U pip
python -m pip install -r requirements.txt
python -m pip install -r requirements-dev.txt

streamlit run app.py
```

---

## ✅ Tooling & workflow

This repo ships with lightweight quality gates:
- **ruff** for linting/formatting
- **pytest** for smoke tests
- **pre-commit** hooks for local consistency
- **GitHub Actions** workflows under `.github/workflows/` to validate PRs

### Lint & format

```bash
python -m ruff check . --fix
python -m ruff format .
```

### Tests

```bash
python -m pytest -q
```

### Pre-commit (recommended)

```bash
pre-commit install
pre-commit run --all-files
```

---

## 🧩 Case study

Read the engineering-focused write-up: [CASE_STUDY.md](CASE_STUDY.md).

---

## 📦 Docker (optional)

```bash
docker build -t visual-lab .
docker run -p 8501:8501 visual-lab
```

Open: http://localhost:8501

---

## 📁 Project structure

```text
.
├─ app.py
├─ requirements.txt
├─ requirements-dev.txt
├─ tests/
├─ assets/                 # README screenshots
└─ .github/workflows/      # CI pipelines
```

---

## 🧠 Notes (production-minded)

- Avoid expensive work at import-time; keep heavy work inside functions. This keeps tests fast and CI stable.
- For major dependency bumps, run the app and click through all tabs before merging.

---

## 📜 License

Apache-2.0 — see [LICENSE](LICENSE).

---

## 👤 Author

Tarek Masryo
