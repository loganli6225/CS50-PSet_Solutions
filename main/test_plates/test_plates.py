from plates import is_valid

def test_correct():
    assert is_valid("CS50") == True

def test_start_two_letters():
    assert is_valid("5050") == False

def test_too_long():
    assert is_valid("CSCSCS50") == False

def test_too_short():
    assert is_valid("A") == False

def test_first_number_zero():
    assert is_valid("CS05") == False

def test_middle_numbers():
    assert is_valid("CS50CS") == False

def test_other_characters():
    assert is_valid("CS .?5") == False
