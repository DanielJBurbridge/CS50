import re

def main():

    user_input = input("Input: ")
    print(shorten(user_input))

def shorten(word):

    VOWELS = '[AEIOUaeiou]'
    return(''.join(re.split(VOWELS, word)))

if __name__ == "__main__":
    main()