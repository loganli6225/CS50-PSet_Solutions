from twttr import shorten

def test_no_vowel():
    assert shorten("_twttr_") == "_twttr_"

def test_a():
    assert shorten("tap") == "tp"

def test_e():
    assert shorten("deer") == "dr"

def test_i():
    assert shorten("mins") == "mns"

def test_o():
    assert shorten("log") == "lg"

def test_u():
    assert shorten("cups") == "cps"

# def test_vowels():
#     assert shorten("altitude_do") == "lttd_d"

def test_uppercase():
    assert shorten("ALTITUDE_DO") == "LTTD_D"

def test_numbers():
    assert shorten("twttr123") == "twttr123"

def test_punctuation():
    assert shorten("!twttr.,") == "!twttr.,"

# def test_other_characters():
#     assert shorten("!twttr123.,") == "!twttr123.,"
