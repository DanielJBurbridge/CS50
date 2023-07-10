import re
import sys

def main():
    print(count(input("Text: ")))

def count(s):
    pattern = re.compile(r'\bum\b|')

    ums = re.findall(pattern, s.lower())

    counter = 0
    for c in ums:
        if c == 'um':
            counter = counter + 1
    return counter


if __name__ == "__main__":
    main()