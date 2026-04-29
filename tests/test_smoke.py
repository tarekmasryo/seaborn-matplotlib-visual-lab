import importlib
import os
import py_compile
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def _parse_version(v: str) -> tuple[int, int]:
    parts = v.strip().split(".")
    if len(parts) < 2:
        raise ValueError("MIN_PYTHON must be like '3.10' or '3.11'")
    return int(parts[0]), int(parts[1])


def test_smoke_python_version():
    min_py = os.getenv("MIN_PYTHON", "3.11")
    assert sys.version_info >= _parse_version(min_py)


def test_smoke_core_imports():
    """
    Fast fail if selected dependencies are broken.

    Keep this opt-in so local syntax checks remain fast and deterministic.
    Configure via:
      SMOKE_IMPORTS="numpy,pandas,streamlit,matplotlib,seaborn,scipy"
    """
    imports = os.getenv("SMOKE_IMPORTS", "")
    if not imports.strip():
        return

    for mod in [m.strip() for m in imports.split(",") if m.strip()]:
        importlib.import_module(mod)


def test_smoke_project_module_importable():
    """
    Optional package-level import check.

    Configure via:
      PROJECT_MODULE="your_package_name"
    """
    module = os.getenv("PROJECT_MODULE", "").strip()
    if not module:
        return
    importlib.import_module(module)


def test_smoke_app_syntax_compiles():
    """
    Streamlit apps execute UI code at module import time.

    Validate syntax without importing app.py, so CI does not depend on network-backed
    dataset loading, Streamlit runtime state, or sidebar execution side effects.
    """
    py_compile.compile(str(ROOT / "app.py"), doraise=True)
