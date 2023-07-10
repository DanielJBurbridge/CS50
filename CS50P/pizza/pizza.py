import sys
import csv
from tabulate import tabulate

def Main():

    expected_command_lines_size = 1
    Validate_Command_Line_Size(expected_command_lines_size + 1)

    expected_file_format = 'csv'
    file_name = sys.argv[1].split(".")
    file_name_prefix = Validate_File_Format(expected_file_format, file_name)

    file = Load_File_To_Memory(file_name_prefix, expected_file_format)

    my_headers='firstrow'
    my_tablefmt='grid'

    print(Tablulate_File(file))

def Validate_Command_Line_Size(x):

    argv = sys.argv
    if len(argv) == x:
        return True
    elif len(argv) < x:
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Too many command-line arguments")

def Validate_File_Format(expected_file_format, file_name):

    if len(file_name) == 1:
        sys.exit("Not a Python file")
    elif file_name[1] != expected_file_format:
        sys.exit("Not a Python file")

    return file_name[0]

def Load_File_To_Memory(file_name_prefix, expected_file_format):

    pizza_prices = {}

    try:
        with open(f'{file_name_prefix}.{expected_file_format}') as file:
            reader = csv.DictReader(file, fieldnames = ["Regular Pizza", "Small", "Large"])
            pizza_prices = [dict(d) for d in reader]


    except FileNotFoundError:
        sys.exit("File not Found")

    return pizza_prices

def Tablulate_File(file, my_headers='firstrow', my_tablefmt='grid'):
    return tabulate(file, headers=my_headers, tablefmt=my_tablefmt)

if __name__ == "__main__":
    Main()
