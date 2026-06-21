import pytest

from speed_tools import braking_distance, kmh_to_ms, ms_to_kmh


def test_kmh_to_ms():
    assert kmh_to_ms(36) == pytest.approx(10.0)


def test_ms_to_kmh():
    assert ms_to_kmh(10) == pytest.approx(36.0)


def test_braking_distance():
    assert braking_distance(20, 2) == pytest.approx(100.0)


def test_braking_distance_invalid_deceleration():
    with pytest.raises(ValueError):
        braking_distance(20, 0)
