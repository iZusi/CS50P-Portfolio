import pytest
from working import convert, convert_to_24

# test cases for convert_to_24 function
def test_convert_to_24():
    assert convert_to_24(12, 30, 'pm') == '12:30'
    assert convert_to_24(3, 15, 'pm') == '15:15'
    assert convert_to_24(12, 45, 'am') == '00:45'
    assert convert_to_24(9, 0, 'am') == '09:00'
    assert convert_to_24(0, 15, 'am') == '00:15'
    with pytest.raises((TypeError, ValueError)):
        convert_to_24('12', '30', 'pm')
        convert_to_24(13, 30, 'am')

# test cases for convert function
def test_convert():
    assert convert("2:15 PM to 3:30 AM") == ('14:15', '03:30')
    assert convert("12:00 PM to 1:45 AM") == ('12:00', '01:45')
    assert convert("8:30 AM to 10:00 PM") == ('08:30', '22:00')
    assert convert("11 PM to 12 AM") == ('23:00', '00:00')
    with pytest.raises((ValueError, SystemExit)):
        convert("25:66 PM to 00:59 PM")
        convert("12 PM to 24 PM")
        convert("abc to def")
    with pytest.raises((TypeError, ValueError)):
        convert(123)
