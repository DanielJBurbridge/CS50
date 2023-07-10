from datetime import date
from datetime import datetime
import re
import sys
import inflect

def main():
    DOB_date = prompt_user_for_date()
    DOB_date = check_valid_date(DOB_date)
    today = get_todays_date()
    difference_in_datetimes = get_datetime_difference(DOB_date, today)
    minutes = convert_days_to_minutes(difference_in_datetimes)
    print(convert_minutes_to_text(minutes))

def prompt_user_for_date():
    return input("date of Birth: ")

def check_valid_date(DOB_date):
    pattern = re.compile(r'^\d{4}-[0-1]{1}[0-9]{1}-[0-3]{1}[0-9]{1}$')

    if not re.match(pattern, DOB_date):
        print("invalid date")
        sys.exit(1)
    year, month, day = DOB_date.split('-')
    # DOB_date = date(int(year), int(month), int(day))
    DOB_date= datetime.strptime(f'{year}-{month}-{day}', '%Y-%m-%d')
    # print(f'date of birth = {DOB_date}')

    if DOB_date >= get_todays_date():
        print("invalid date")
        sys.exit(1)

    return DOB_date

def get_todays_date():
    return datetime.strptime(date.today().strftime('%Y-%m-%d'), '%Y-%m-%d')

def get_datetime_difference(date1, date2):
    # print(date2 - date1)
    return (date2 - date1)

def calculate_difference_in_days_between_dates(date):
    return date.days()

def convert_days_to_minutes(date):
    return int(date.total_seconds() / 60)

def convert_minutes_to_text(minutes):
    inflect_engine = inflect.engine()
    return (inflect_engine.number_to_words(minutes, andword="") + " minutes").capitalize()


if __name__ == '__main__':
    main()