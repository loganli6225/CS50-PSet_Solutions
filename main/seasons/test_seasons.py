from seasons import mins_from
import pytest

def test_invalid_format():
    with pytest.raises(SystemExit):
        mins_from("June 2, 2005")
    with pytest.raises(SystemExit):
        mins_from("06/02/2005")
    with pytest.raises(SystemExit):
        mins_from("06-02-2005")

def test_invalid_date():
    with pytest.raises(SystemExit):
        mins_from("2005-13-32")

def test_date_2024_08_04():
    assert mins_from("2023-08-04") == "Five hundred twenty-seven thousand forty minutes"
