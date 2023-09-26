from plates import is_valid


# Test cases for is_valid function
def test_invalid_length():
    assert is_valid("A") == False

def test_valid_input_with_special_character():
    assert is_valid("AB-123") == False

def test_valid_input_no_characters():
    assert is_valid("123456") == False

# Test cases for zero placement
def test_valid_zero_placement():
    assert is_valid("ABC01") == False

def test_invalid_zero_placement_beginning():
    assert is_valid("0ABC1") == False

def test_invalid_zero_placement_middle():
    assert is_valid("AB0C1") == False

def test_invalid_zero_placement_repeating():
    assert is_valid("AB00C") == False

# Test cases for number placement
def test_valid_number_placement_end():
    assert is_valid("AAA222") == True

def test_invalid_number_placement_middle():
    assert is_valid("AAA22A") == False

def test_invalid_number_placement_beginning():
    assert is_valid("1AAA22") == False

def test_invalid_number_placement_repeating():
    assert is_valid("1AAA222") == False
