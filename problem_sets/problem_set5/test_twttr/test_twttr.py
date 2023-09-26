from twttr import shorten

# check for lowercase
def test_lowercase():
    assert shorten("hello") == "hll"

# check for uppercase
def test_uppercase():
    assert shorten("HELLO") == "HLL"

# check for integers
def test_integers():
    assert shorten("12345") == "12345"

# check for special characters
def test_special_char():
    assert shorten("!@,#$%") == "!@,#$%"
