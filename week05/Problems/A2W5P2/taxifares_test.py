import pytest
from taxifares import calculate_fare


def test_calculate_fare():
    distance = 2
    expected_fare = 7.7
    assert calculate_fare(distance) == expected_fare

    distance = 1.4
    expected_fare = 6.5
    assert calculate_fare(distance) == expected_fare


def test_negative_distance():
    distance = -1
    with pytest.raises(ValueError):
        calculate_fare(distance)


def non_numeric_input():
    distance = "hello"
    with pytest.raises(TypeError):
        calculate_fare(distance)
