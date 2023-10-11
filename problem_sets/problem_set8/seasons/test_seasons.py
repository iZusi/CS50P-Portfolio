import pytest
from seasons import get_birthday

def test_get_birthday():
    assert get_birthday("2000-01-01") == "Fourteen million, nine hundred five thousand, four hundred forty minutes"

# testing invalid input
def test_invalid_input():
    with pytest.raises(SystemExit):
        get_birthday('01-01-2021')
