def main():

    fraction = input("Fraction: ")
    try:
        percentage = convert_fraction(fraction)
    except (ValueError, ZeroDivisionError):
        main()

    output(percentage)

def convert_fraction(s):
    numbers =  s.split("/")
    numbers[0] = int(numbers[0])
    numbers[1] = int(numbers[1])

    if numbers[0] > numbers[1]:
       main()

    percentage = round(numbers[0] / numbers[1] * 100)

    return percentage

def output(p):
    output_as_string = ""

    if p >= 99:
        output_as_string = "F"
    elif p <= 1:
        output_as_string = "E"
    else:
        output_as_string = f'{p}%'


    print(output_as_string)



if __name__ == "__main__":
    main()