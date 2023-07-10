import re
def main():
    user_input = input("IPv4 Address: ")

    if validate(user_input):
        print("True")
    else:
        print("False")

def validate(ip):
    expected_length = 4

    format_validated = Validate_Format(ip)
    if not format_validated:
        return False

    length_validated = Validate_Length(ip, expected_length)
    range_validated = Validate_Range(ip)

    return length_validated and range_validated

def Validate_Format(ip):
    valid_format = r'^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$'
    return bool(re.match(valid_format, ip))

def Validate_Length(ip, expected_length=4):
    ip_length = len(ip.split('.'))
    return ip_length == expected_length

def Validate_Range(ip):
    ip_split = ip.split('.')
    return all(map(lambda x: 0 <= int(x) <= 255, ip_split))

if __name__ == "__main__":
    main()