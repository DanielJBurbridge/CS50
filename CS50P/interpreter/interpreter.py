user_input = input("Math Problem: " )
equation = user_input.split(" ")
symbols = ["+", "-", "/", "*"]

if "+" == equation[1]:
    print("{:.1f}".format(float(float(equation[0]) + float(equation[2]))))
elif "-" == equation[1]:
    print("{:.1f}".format(float(float(equation[0]) - float(equation[2]))))
elif "/" == equation[1]:
    print("{:.1f}".format(float(float(equation[0]) / float(equation[2]))))
elif "*" == equation[1]:
    print("{:.1f}".format(float(float(equation[0]) * float(equation[2]))))
