import re

def main():
    user_input = input("Provide Camel Case: ")
    print(convert_to_snake(user_input, "(?=[A-Z])"))

def convert_to_snake(text, pattern):
    return '_'.join(re.split(pattern, text)).lower()


if __name__ == "__main__":
    main()