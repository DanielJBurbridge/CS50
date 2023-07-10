def main():

    paid = 0
    threshold = 50

    while paid < threshold:

        coin = input("Insert Coin: ")

        if (coin == str(25)):
            paid += 25
        elif (coin == str(10)):
            paid += 10
        elif (coin == str(5)):
            paid += 5

        due = threshold - paid

        if due > 0:
            print("Amount Due: " + str(due))

    print('Change Owed: ' + str(paid - threshold))



if __name__ == "__main__":
    main()