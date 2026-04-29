# Changelog

## 1.0.1
- Reformatted application code so Ruff format checks pass in CI.
- Tightened the CI workflow to validate the Streamlit app, tests, and utility scripts without unnecessary Docker build noise.
- Updated Seaborn lower bound to `>=0.13.2` and aligned Ruff pre-commit hook version with dev requirements.
- Removed automated Dependabot configuration to avoid noisy dependency PRs for this lightweight portfolio repo.

## 1.0.0
- Added Streamlit visual lab for Seaborn and Matplotlib workflows.
- Added dataset overview, Seaborn builder, Matplotlib builder, comparison view, and gallery export.
- Added deterministic fallback dataset for resilient first-run behavior when Seaborn example data cannot be reached.
- Added lightweight quality gates with Ruff, pytest, pre-commit, GitHub Actions, and Docker build stages.
- Added README screenshots, case study, contribution guide, security notes, and Apache-2.0 license.
