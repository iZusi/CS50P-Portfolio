import pytest
from fuel import convert, gauge

# Test cases for convert() function
def test_convert_valid_fraction():
    assert convert("3/4") == 75

def test_convert_zero_denominator():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_convert_non_integer_x():
    with pytest.raises(ValueError):
        convert("abc/2")

def test_convert_non_integer_y():
    with pytest.raises(ValueError):
        convert("1/xyz")

def test_convert_x_greater_than_y():
    with pytest.raises(ValueError):
        convert("5/3")

# Test cases for gauge() function
def test_gauge_e():
    assert gauge(1) == "E"

def test_gauge_below_1():
    assert gauge(0) == "E"

def test_gauge_f():
    assert gauge(99) == "F"

def test_gauge_over_99():
    assert gauge(100) == "F"

def test_gauge_percent():
    assert gauge(50) == "50%"
