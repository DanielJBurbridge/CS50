from pyfiglet import Figlet
import pyfiglet
import sys
import random

def main(myfont):
    # print(pyfiglet.FigletFont.getFonts())
    user_input = input("Input: ")
    f = Figlet(font=myfont)
    print("Output:")
    print(f.renderText(user_input))

if __name__ == "__main__":
    myfonts = ["slant", "rectangles", "alphabet"]
    if len(sys.argv) == 3:
        if sys.argv[1] == "-f" or sys.argv[2] == "--font":
            # print(sys.argv[2][1:])
            if sys.argv[2] in pyfiglet.FigletFont.getFonts() or sys.argv[2] in myfonts:
                main(sys.argv[2][1:])
            else:
                sys.exit("Invalid usage")
        else:
            sys.exit("Invalid usage")
    elif len(sys.argv) == 1:
        main(random.choice(pyfiglet.FigletFont.getFonts()))
    else:
        sys.exit("Invalid usage")
