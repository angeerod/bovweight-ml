import pytest
from app.predictor import estimate_weight


def test_known_weight():
    # Girth=180, Length=150 → (180^2 * 150) / 10800 = 450 kg
    result = estimate_weight(140, 150, 180)
    assert abs(result - 450.0) < 0.01


def test_negative_measurement_raises():
    with pytest.raises(ValueError):
        estimate_weight(-1, 150, 180)


def test_zero_measurement_raises():
    with pytest.raises(ValueError):
        estimate_weight(140, 0, 180)


def test_small_calf():
    result = estimate_weight(80, 90, 110)
    assert result > 0
