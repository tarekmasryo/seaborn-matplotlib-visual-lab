import pytest

from visual_lab_core import capped_sample_size, pairplot_sample_bounds


def test_pairplot_sample_bounds_handle_small_datasets():
    min_rows, max_rows, default_rows = pairplot_sample_bounds(52)

    assert min_rows == 1
    assert max_rows == 52
    assert default_rows == 52
    assert min_rows <= default_rows <= max_rows


def test_pairplot_sample_bounds_handle_large_datasets():
    min_rows, max_rows, default_rows = pairplot_sample_bounds(5000)

    assert min_rows == 100
    assert max_rows == 1000
    assert default_rows == 400
    assert min_rows <= default_rows <= max_rows


def test_capped_sample_size_uses_available_post_dropna_rows():
    assert capped_sample_size(requested_rows=400, available_rows=12) == 12
    assert capped_sample_size(requested_rows=50, available_rows=0) == 0


def test_pairplot_sample_bounds_reject_invalid_values():
    with pytest.raises(ValueError):
        pairplot_sample_bounds(-1)
