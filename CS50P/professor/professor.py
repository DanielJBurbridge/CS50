import random

def main():
    level = int(get_level())
    problem_set = generate_problem_set(level)
    quiz(problem_set)

def quiz(problem_set):

    correct_answers = 0

    for problem in problem_set:
        guess_count = 0
        guess_limit = 3

        while guess_count < guess_limit:
            guess = input(f'{problem[0]} + {problem[1]} = ')
            if guess == str(problem[2]):
                correct_answers += 1
                break
            else:
                print("EEE")
                guess_count += 1
        if guess_count == 3:
            print(f'{problem[0]} + {problem[1]} = {problem[2]}')

    print(f'Score: {correct_answers}')



def get_level():
    validated = False

    while not validated:
        level = input("Level: ")
        validated = validator(level)

    return level

def generate_problem_set(level):
    problem_count = 10
    problem_set = []
    for _ in range(problem_count):
        problem_set.append(generate_problem(level))

    return problem_set

def generate_problem(level):
    problem = []
    problem.append(generate_integer(level))
    problem.append(generate_integer(level))
    problem.append(problem[0] + problem[1])
    return problem

def generate_integer(level):
    floor = generate_floor(level)
    ceil = generate_ceiling(level)
    return random.randrange(floor, ceil)


def generate_floor(level):
    try:
        if level == 1:
            return 0
        elif level == 2:
            return  10
        elif level == 3:
            return 100
    except ValueError:
        raise(ValueError)

def generate_ceiling(level):
    try:
        if level == 1:
            return 10
        elif level == 2:
            return  100
        elif level == 3:
            return 1000
    except ValueError:
        raise(ValueError)

def validator(i):

    try:
        if int(i) == 1 or int(i) == 2 or int(i) == 3:
            return True
        else:
            return False
    except:
        return False

if __name__ == "__main__":
    main()
