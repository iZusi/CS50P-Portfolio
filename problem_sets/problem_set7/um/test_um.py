from um import count

# test cases for count function
def test_count():
    assert count("UM") == 1
    assert count("") == 0
    assert count("Um um ummm UMMM") == 2
