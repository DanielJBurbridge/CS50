import re

def main():
    user_input = input("What time is it? ")

    formated_time = format_time(user_input)
    time = convert(formated_time)

    if time >= 7 and time <= 8:
        print("breakfast time")
    elif time >= 12 and time <= 13:
        print("lunch time")
    elif time >= 18 and time <= 19:
        print("dinner time")

def format_time(time):
    am_pm_checker = '.*[am|pm]$'
    am = '.*am$'
    pm = '.*pm$'

    if bool(re.match(am_pm_checker, time)):
        hour = time.split(":")[0]
        minute = time.split(":")[1]

        if bool(re.match(am, time)):
            minute = minute.split("a")[0]
            hour = int(hour)
            if hour == 12:
                hour = hour - 12
            hour = str(hour)
        elif bool(re.match(pm, time)):
            minute = minute.split("p")[0]
            hour = int(hour)
            if hour == 12:
                hour = hour
            else:
                hour = hour + 12
            hour = str(hour)
        return hour + ":" + minute
    else:
        return time


def convert(time):
    values = time.split(":")
    hour = float(values[0])
    minutes = float(values[1]) / 60
    valued_times = hour + minutes
    return valued_times

if __name__ == "__main__":
    main()