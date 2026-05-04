# Case Study — Seaborn + Matplotlib Visual Lab

## Problem
Learning data visualization is usually split between two extremes: high-level Seaborn recipes and low-level Matplotlib control. The goal was one interactive lab that makes the comparison concrete and fast:

- How does the same chart idea look in Seaborn vs Matplotlib?
- What UI parameters matter (bins, hue, order, figure size, grids, themes)?
- Can I export clean figures (PNG) and keep a reusable gallery?

## Approach
- Streamlit app with a “builder” workflow: pick dataset → pick chart → tweak controls → view plot + generated code.
- Seaborn builder for statistical plots (distributions, relationships, categories, heatmaps, pairplots).
- Matplotlib builder to recreate the same ideas with the low-level API (axes/layout control).
- Compare tab to show side-by-side outputs for the same visualization intent.
- Gallery tab to save figures and export PNGs or a ZIP bundle.

## Key Decisions
- **One-click datasets:** load classic Seaborn example datasets (tips, penguins, flights, iris, diamonds sample, titanic, car_crashes).
- **Offline-friendly fallback:** if Seaborn’s online dataset catalog cannot be reached, fall back to a small built-in dataset to keep the UI usable.
- **Export-first design:** every chart can be saved to a local gallery and exported (PNG / ZIP) without manual code edits.
- **Engineering hygiene:** Ruff + pytest + pre-commit + GitHub Actions for consistent formatting and smoke tests.

## Results
An interactive visualization lab that supports:
- Dataset overview (dtypes, missingness, correlation glimpse)
- UI-driven Seaborn charts + auto-updating code snippet
- UI-driven Matplotlib charts with layout/axes controls
- Side-by-side comparison (Seaborn vs Matplotlib)
- Gallery + PNG/ZIP export for sharing and documentation

## Next Steps
- Add user CSV upload + schema preview (keep the example datasets as presets).
- Add “style presets” (publication, dark, minimal) and figure templates.
- Add a lightweight report export (HTML/PDF) that bundles selected gallery figures + captions.
