import re

def main():
    print(f'${value(input("Greeting: ").strip().lower())}')


def value(greeting):

    responses = ["^hello.*", "^h.*", "."]
    matrix = []

    for response in responses:
        matrix.append(bool(re.match(response, greeting)))

    if matrix[0]:
        return 0
    elif matrix[1]:
        return 20
    elif matrix[2]:
        return 100

if __name__ == "__main__":
    main()