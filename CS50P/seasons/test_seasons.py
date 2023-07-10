#CHATGPT was used in writing these tests with a few tweaks
import pytest
from datetime import datetime, timedelta
from seasons import check_valid_date, get_todays_date, get_datetime_difference, convert_days_to_minutes, convert_minutes_to_text

# Test check_valid_date function
def test_check_valid_date():
    # Test a valid date
    assert check_valid_date('1990-01-01') == datetime(1990, 1, 1)

    # Test an invalid date format
    with pytest.raises(SystemExit):
        check_valid_date('01-01-1990')

    # Test an invalid date in the future
    with pytest.raises(SystemExit):
        check_valid_date('2025-01-01')

# Test get_todays_date function
def test_get_todays_date():
    today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    assert get_todays_date() == today

# Test get_datetime_difference function
def test_get_datetime_difference():
    date1 = datetime(2021, 1, 1)
    date2 = datetime(2021, 1, 2)
    difference = timedelta(days=1)
    assert get_datetime_difference(date1, date2) == difference

# Test convert_days_to_minutes function
def test_convert_days_to_minutes():
    days = timedelta(days=2)
    minutes = 2880
    assert convert_days_to_minutes(days) == minutes

# Test convert_minutes_to_text function
def test_convert_minutes_to_text():
    assert convert_minutes_to_text(60) == "Sixty minutes"
    assert convert_minutes_to_text(120) == "One hundred twenty minutes"

    # Test upper limit
    assert convert_minutes_to_text(999999) == "Nine hundred ninety-nine thousand, nine hundred ninety-nine minutes"

    # Test lower limit
    assert convert_minutes_to_text(0) == "Zero minutes"