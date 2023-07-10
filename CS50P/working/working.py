import re

def main():

    print(convert(input("Hours: ")))


# def main():
#     tests = [
#         '12:00 AM to 12:00 PM',
#         '1 PM to 5 PM',
#         '12:30 AM to 2:15 PM',
#         '12:50 PM to 02:08 AM',
#         '12 PM to 2:59 PM'
#     ]

#     for test in tests:
#         print(convert(test))


def convert(s):

    regex_match = test_expected_input(s)
    time_one, time_two = seperate_string_to_times(regex_match)
    time_one = convert_to_24hour_format(time_one)
    time_two = convert_to_24hour_format(time_two)
    return generate_output(time_one, time_two)


def test_expected_input(s):
    pattern_expected_input = re.compile(r'(?P<one>([0-1]{0,1}[0-9])(:[0-5][0-9]){0,1} (AM|PM)) to (?P<two>([0-1]{0,1}[0-9])(:[0-6][0-9]){0,1} (AM|PM))')
    result = re.match(pattern_expected_input, s)

    if not result:
        raise ValueError("This is not an expected input")

    return result


def seperate_string_to_times(regex_match):
    time_one_raw, time_two_raw = regex_match.group('one'), regex_match.group('two')
    time_one = segment_data(time_one_raw)
    time_two = segment_data(time_two_raw)
    return time_one, time_two


def segment_data(time_raw):

    if ":" in time_raw:
        time_hours = (time_raw.split(':')[0]).zfill(2)
        time_minutes = (time_raw.split(':')[1][0:-3])
        time_qualifier = (time_raw.split(':')[1][-2:])
    else:
        time_hours = time_raw.split(' ')[0].zfill(2)
        time_minutes = '00'
        time_qualifier = (time_raw.split(' ')[1])

    return [time_hours, time_minutes, time_qualifier]


def convert_to_24hour_format(time):
    if time[2] == 'AM':
        if time[0] == '12':
            time[0] = '00'

    if time[2] == 'PM':
        if time[0] == '12':
            time[0] = '12'
        else:
            time[0] = str(int(time[0]) + 12)

    return time


def generate_output(time_one, time_two):
    return f'{time_one[0]}:{time_one[1]} to {time_two[0]}:{time_two[1]}'

if __name__ == '__main__':
    main()