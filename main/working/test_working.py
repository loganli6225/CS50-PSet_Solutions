from working import convert
import pytest

def test_correct_case_1():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9:30 AM to 5:30 PM") == "09:30 to 17:30"

def test_correct_case_2():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test_correct_case_3():
    assert convert("9:00 AM to 5 PM") == "09:00 to 17:00"
    assert convert("10:30 PM to 8 AM") == "22:30 to 08:00"

def test_correct_case_4():
    assert convert("9 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 AM to 8:50 PM") == "10:00 to 20:50"

def test_wrong_format():
    with pytest.raises(ValueError):
        convert("9 AM - 5:00 PM")

def test_invalid_times():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert("09:00 AM to 17:00 PM")
