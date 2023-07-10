import re

def main():
    user_input = input("Input: ")

    vowels = '[AEIOUaeiou]'

    output = ''.join(re.split(vowels, user_input))

    print(output)



if __name__ == "__main__":
    main()