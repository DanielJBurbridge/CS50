import pytest
from working import convert

def test_convert():
    assert convert('12:00 AM to 12:00 PM') == '00:00 to 12:00'
    assert convert('1 PM to 5 PM') == '13:00 to 17:00'
    assert convert('12:30 AM to 2:15 PM') == '00:30 to 14:15'
    assert convert('12:50 PM to 02:08 AM') == '12:50 to 02:08'
    assert convert('12 PM to 2:59 PM') == '12:00 to 14:59'

def test_convert_invalid_input():
    with pytest.raises(ValueError):
        convert('Invalid input')
    with pytest.raises(ValueError):
        convert('11:89 PM to 45:32 AM')