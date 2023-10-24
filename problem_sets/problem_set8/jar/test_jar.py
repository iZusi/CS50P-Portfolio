import pytest
from jar import Jar


def test_init():
    test_jar = Jar()    # create instance from Jar class
    assert test_jar._capacity == 12
    assert test_jar.cookies == 0


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    test_jar = Jar()
    with pytest.raises(ValueError):
        test_jar.deposit(13)


def test_withdraw():
    test_jar = Jar()
    with pytest.raises(ValueError):
        test_jar.withdraw(2)
