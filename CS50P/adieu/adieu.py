import inflect

def main():

    p = inflect.engine()
    names = []

    while True:
    # while len(names) < 4:
        try:
            names.append(input("").strip())
        except EOFError:
            break

    print(f'Adieu, adieu, to {p.join(names)}')


if __name__ == '__main__':
    main()