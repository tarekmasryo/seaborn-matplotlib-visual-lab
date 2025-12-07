# 📊 Seaborn & Matplotlib Visual Lab

[![Streamlit](https://img.shields.io/badge/Powered%20by-Streamlit-FF4B4B)](https://streamlit.io/)<br>
[![Made with ❤️ by Tarek Masryo](https://img.shields.io/badge/Made%20by-Tarek%20Masryo-blue)](https://github.com/tarekmasryo)

An interactive **Streamlit** lab for learning and comparing **Seaborn** and **Matplotlib** — build plots from UI controls, see the code, and export clean PNGs.

---

## 🧪 What this app does

This app is a small **visual lab for plots**:

- Load classic **Seaborn demo datasets** in one click (Tips, Penguins, Flights, Iris, Diamonds, Titanic, Car Crashes).
- Build **Seaborn** charts (distribution, relationship, category, heatmaps, pairplots) through simple controls.
- Recreate the same ideas with **Matplotlib** and see the low-level API.
- Compare Seaborn vs Matplotlib **side by side** on the same pattern.
- Save any figure to a **gallery** and export PNGs or a ZIP archive.

Perfect for **learning**, **teaching**, and **quick EDA prototypes**.

---

## 🧭 App Structure

| Tab | Purpose |
|:---|:--------|
| **Overview** | Quick health check: sample, types, missingness, and a small correlation heatmap. |
| **Seaborn builder** | UI-driven Seaborn plots with auto-updating Python snippets. |
| **Matplotlib builder** | Low-level Matplotlib plots with control over axes, grids, and layout. |
| **Compare** | Same idea shown once with Seaborn and once with Matplotlib. |
| **Gallery** | Saved figures, PNG download, and ZIP export. |

---

## 📚 Data Sources

All datasets come from **Seaborn’s built-in catalog**, no external files needed:

- `tips`
- `penguins` (cleaned)
- `flights`
- `iris`
- `diamonds` (1K sample)
- `titanic`
- `car_crashes`

---

## 📸 Dashboard Preview

### 1️⃣ Seaborn — Distribution Builder (Tips)

<p align="center">
  <img src="assets/seaborn-tips-total-bill-hist-sex.png" alt="Seaborn histogram of total_bill by sex from the tips dataset" />
</p>

---

### 2️⃣ Seaborn — Relationship Builder (Tips)

<p align="center">
  <img src="assets/seaborn-tips-total-bill-vs-tip-scatter.png" alt="Seaborn scatter plot of total_bill vs tip from the tips dataset" />
</p>

---

### 3️⃣ Matplotlib — Histogram (Iris)

<p align="center">
  <img src="assets/matplotlib-iris-sepal-length-hist.png" alt="Matplotlib histogram of sepal length from the iris dataset" />
</p>

---

### 4️⃣ Matplotlib — Line Plot (Iris)

<p align="center">
  <img src="assets/matplotlib-iris-sepal-length-line.png" alt="Matplotlib line plot of sepal length over index from the iris dataset" />
</p>

---

### 5️⃣ Compare — Histogram + KDE (Tips)

<p align="center">
  <img src="assets/compare-hist-kde-tips.png" alt="Compare tab showing Seaborn vs Matplotlib histogram + KDE for the tips dataset" />
</p>

---

### 6️⃣ Compare — Scatter (Flights)

<p align="center">
  <img src="assets/compare-scatter-flights.png" alt="Compare tab showing Seaborn vs Matplotlib scatter plot for the flights dataset" />
</p>

---

## 🚀 Quick Start

```bash
# clone the repo
git clone https://github.com/tarekmasryo/seaborn-matplotlib-visual-lab.git
cd seaborn-matplotlib-visual-lab

# (optional) create venv
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux / macOS
source .venv/bin/activate

# install dependencies
pip install -r requirements.txt

# run the app
streamlit run app.py

```

---

## 💡 When is this useful?

- Teaching Seaborn vs Matplotlib in workshops or classes.
- Trying different plot families **before** copying code into a notebook.
- Building small **code snippets** for reports, blogs, or EDA templates.
- Playing with themes, palettes, and structures without editing Python by hand.

If you enjoy the lab, consider giving the repo a ⭐ to support more visual tools like this.
