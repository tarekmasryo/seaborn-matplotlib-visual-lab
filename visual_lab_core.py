"""Small pure-Python helpers for Streamlit UI edge cases."""


def pairplot_sample_bounds(
    row_count: int,
    *,
    soft_min_rows: int = 100,
    hard_max_rows: int = 1000,
    default_rows: int = 400,
) -> tuple[int, int, int]:
    """Return valid Streamlit slider bounds for pairplot sampling.

    Streamlit sliders require min <= value <= max. Small datasets such as
    Seaborn's car_crashes dataset have fewer than 100 rows, so a fixed
    min_value=100 can crash the UI.
    """
    if row_count < 0:
        raise ValueError("row_count must be non-negative")
    if soft_min_rows < 1:
        raise ValueError("soft_min_rows must be positive")
    if hard_max_rows < 1:
        raise ValueError("hard_max_rows must be positive")
    if default_rows < 1:
        raise ValueError("default_rows must be positive")

    max_rows = max(1, min(row_count, hard_max_rows))
    min_rows = 1 if max_rows < soft_min_rows else soft_min_rows
    value = min(default_rows, max_rows)
    return min_rows, max_rows, value


def capped_sample_size(requested_rows: int, available_rows: int) -> int:
    """Return a safe sample size for a dataframe after filtering/dropna."""
    if requested_rows < 1:
        raise ValueError("requested_rows must be positive")
    if available_rows < 0:
        raise ValueError("available_rows must be non-negative")
    return min(requested_rows, available_rows)
