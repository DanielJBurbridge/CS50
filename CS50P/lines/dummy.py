import sys
import csv

def Main():

   lines = []
   file_name = sys.argv[1]


   with open(f'{file_name}.py') as file:
       for line in file:
           lines.append(line.rstrip())
           #I don't fully understand

    print(lines)




if __name__ == "__main__":

    argv = sys.argv
    if len(argv) == 2:
        Main()
    else:
        sys.exit("Too few command-line arguments")