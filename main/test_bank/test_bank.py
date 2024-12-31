from bank import value

def test_hello():
    assert value("hello, world") == 0
def test_h():
    assert value("hi") == 20
def test_other():
    assert value("other greeting") == 100

def test_uppercase_hello():
    assert value("heLLo, WoRLD") == 0
def test_uppercase_h():
    assert value("Hi") == 20
def test_uppercase_other():
    assert value("OtHeR, GreeTiNG") == 100
