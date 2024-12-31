from jar import Jar
import pytest

def test_init_default():
    jar1 = Jar()
    assert jar1.capacity == 12
    assert jar1.size == 0

def test_init_non_neg():
    jar2 = Jar(20)
    assert jar2.capacity == 20
    assert jar2.size == 0

def test_init_neg():
    with pytest.raises(ValueError):
        Jar(-3)

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(1)
    assert jar.size == 1
    jar.deposit(11)
    assert jar.size == 12

def test_deposit_error():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.deposit(13)

def test_withdraw():
    jar = Jar()
    jar.deposit(12)
    jar.withdraw(1)
    assert jar.size == 11
    jar.withdraw(11)
    assert jar.size == 0

def test_withdraw_error():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.withdraw(1)
