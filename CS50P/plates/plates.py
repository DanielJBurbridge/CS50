import re

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    valid_plate = '^[a-zA-Z]{2}[^0-9]{0,4}[0-9]{0,4}$'
    numbers = '[0-9]'
    numbers_not_zero = '[1-9]'

    matched = bool(re.match(valid_plate, s))

    if matched:
        if len(s) <= 6:
            if not bool(re.search(numbers, s)):
                return True
            else:
                for c in s:
                    if bool(re.match(numbers, c)):
                        return bool(re.match(numbers_not_zero, c))
        else:
            return False



    return False

if __name__ == "__main__":
    main()