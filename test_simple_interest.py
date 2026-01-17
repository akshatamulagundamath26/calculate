from simple_interest import calculate_simple_interest


def test_simple_interest_basic():
    assert calculate_simple_interest(1000, 10, 1) == 100.0


def test_simple_interest_zero_rate():
    assert calculate_simple_interest(2000, 0, 5) == 0.0


def test_simple_interest_decimal_values():
    assert calculate_simple_interest(1500, 7.5, 2) == 225.0
