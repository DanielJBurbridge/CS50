from collections import OrderedDict
def main():

    grocery_list = make_dict()
    grocery_list = user_loop(grocery_list)
    grocery_list = sort_dict(grocery_list)
    print_dict(grocery_list)

def user_loop(gl):

    while True:
        try:
            user_input = input("").upper()
            if user_input in gl:
                gl = increment_dict(gl, user_input)
            else:
                gl = add_to_dict(gl, user_input)

        except EOFError:
            break

    return gl

def make_dict():
    return {}

def increment_dict(gl, item):
    gl[item] = gl.get(item) + 1
    return gl

def add_to_dict(gl, item):
    gl[item] = 1
    return gl

def sort_dict(gl):
    return OrderedDict(sorted(gl.items()))

def print_dict(gl):
    for key, value in gl.items():
        print(f"{value} {key}")

if __name__ == "__main__":
    main()