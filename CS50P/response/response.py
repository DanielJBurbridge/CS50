from validator_collection import checkers

def main():
    if not check_valid_email(input("What's your email address? ")):
        print("Invalid")
    else:
        print("Valid")

def check_valid_email(email):
    return checkers.is_email(email)

if __name__ == '__main__':
    main()
