from fuel import convert
from fuel import gauge
import pytest

def test_convert_intended():
    assert convert("3/4") == 75

def test_convert_x_and_or_y_not_int():
    with pytest.raises(ValueError):
        convert("cat/4")
    with pytest.raises(ValueError):
        convert("3/cat")
    with pytest.raises(ValueError):
        convert("cat/dog")

def test_convert_x_greater_y():
    with pytest.raises(ValueError):
        convert("5/4")

def test_convert_y_is_zero():
    with pytest.raises(ZeroDivisionError):
        convert("4/0")

def test_gauge_less_1():
    assert gauge(0.5) == "E"
    assert gauge(1) == "E"

def test_gauge_more_99():
    assert gauge(99.5) == "F"
    assert gauge(99) == "F"

def test_gauge_other():
    assert gauge(50) == "50%"
