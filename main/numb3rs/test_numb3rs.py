from numb3rs import validate

def test_correct():
    assert validate("127.0.0.1") == True

def test_string():
    assert validate("cat") == False

def test_no_three_dots():
    assert validate("0.0") == False
    assert validate("0.0.0") == False
    assert validate("0.0.0.0.0") == False

def test_first_more_than_255():
    assert validate("275.3.6.28") == False
    assert validate("1000.3.6.28") == False

def test_second_more_than_255():
    assert validate("3.275.6.28") == False
    assert validate("3.1000.6.28") == False

def test_third_more_than_255():
    assert validate("6.3.275.28") == False
    assert validate("6.3.1000.28") == False

def test_fourth_more_than_255():
    assert validate("28.3.6.275") == False
    assert validate("28.3.6.1000") == False
