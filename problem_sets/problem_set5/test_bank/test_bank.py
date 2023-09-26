from bank import value


# test for the value in "hello"
def test_hello_value():
    assert value("hello") == 0


# test for the value of just "h"
def test_h_value():
    assert value("hey") == 20


# test for the value in no "h" or "hello"
def test_no_h_hello_value():
    assert value("good day") == 100


# test for the value in mixedcase "hello"
def test_mixedcase_hello_value():
    assert value("Hello") == 0


# test for the value in uppercase "hello"
def test_uppercase_hello_value():
    assert value("HELLO") == 0


# test for the value in mixedcase "Hello"
def test_uppercase_h_value():
    assert value("Hey") == 20


# test for the mixedcase value in no "h" or "hello"
def test_no_mixedcase_h_hello_value():
    assert value("Good Morning") == 100


# test for the uppercase value in no "h" or "hello"
def test_no_uppercase_h_hello_value():
    assert value("GOOD MORNING") == 100
