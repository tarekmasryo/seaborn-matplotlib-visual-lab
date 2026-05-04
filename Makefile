.PHONY: help install dev run lint lint-fix format test check precommit

PY ?= python
APP_FILE ?= app.py

help:
	@echo "Targets:"
	@echo "  install      Install runtime deps (requirements.txt if present)"
	@echo "  dev          Install dev deps (requirements-dev.txt if present)"
	@echo "  run          Run app (Streamlit by default)"
	@echo "  lint         Run ruff lint"
	@echo "  lint-fix     Run ruff lint with fixes"
	@echo "  format       Format code with ruff"
	@echo "  check        Compile + lint + format check + tests"
	@echo "  test         Run pytest"
	@echo "  precommit    Install pre-commit hooks"

install:
	$(PY) -m pip install -U pip
ifneq ($(wildcard requirements.txt),)
	$(PY) -m pip install -r requirements.txt
endif
	@$(PY) -m pip check || true

dev:
	$(PY) -m pip install -U pip
ifneq ($(wildcard requirements-dev.txt),)
	$(PY) -m pip install -r requirements-dev.txt
endif
	@$(PY) -m pip check || true

run:
	$(PY) -m streamlit run $(APP_FILE)

lint:
	$(PY) -m ruff check .

lint-fix:
	$(PY) -m ruff check . --fix --exit-non-zero-on-fix

format:
	$(PY) -m ruff format .

test:
	PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 $(PY) -m pytest tests -q

check:
	$(PY) -m compileall -q app.py visual_lab_core.py tests scripts
	$(PY) -m ruff check .
	$(PY) -m ruff format --check .
	PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 $(PY) -m pytest tests -q

precommit:
	$(PY) -m pip install -U pre-commit
	pre-commit install
