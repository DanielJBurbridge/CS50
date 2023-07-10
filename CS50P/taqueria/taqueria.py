def main():

    menu = generate_menu(1)
    total = 0

    while True:

        try:
            user_input = input("Item: ")
            user_input = user_input.lower().title()
            total += menu.get(user_input)
            print(f"Total: ${total:.2f}")

        except EOFError:
            break

        except:
            pass

def generate_menu(i):

    if i == 1:

        return {
            "Baja Taco": 4.00,
            "Burrito": 7.50,
            "Bowl": 8.50,
            "Nachos": 11.00,
            "Quesadilla": 8.50,
            "Super Burrito": 8.50,
            "Super Quesadilla": 9.50,
            "Taco": 3.00,
            "Tortilla Salad": 8.00
        }

    return None


if __name__ == "__main__":
    main()