import random

def main():

    validated = False

    while not validated:
        level = input("Level: ")
        validated = validator(level)

    answer = generate_answer(level)
    correct = False

    while not correct:
        validated = False
        while not validated:
            guess = input("Guess: ")
            validated = validator(guess)
        if int(guess) > answer:
            print("Too large!")
        elif int(guess) < answer:
            print("Too small!")
        else:
            print("Just right!")
            correct = True


def validator(i):

    try:
        if int(i) > 0:
            return True
        else:
            return False
    except:
        return False

def generate_answer(i):

    return random.randrange(1, int(i) + 1)








if __name__ == "__main__":
    main()


