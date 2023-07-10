import sys
import csv
from tabulate import tabulate


def Main():

    expected_command_lines_size = 2
    Validate_Command_Line_Size(expected_command_lines_size + 1)

    expected_file_format = 'csv'

    input_file_name = sys.argv[1].split(".")
    input_file_name_prefix = Validate_File_Format(expected_file_format, input_file_name)

    output_file_name = sys.argv[2].split(".")
    output_file_name_prefix = Validate_File_Format(expected_file_format, output_file_name)

    file = Load_File_To_Memory(input_file_name_prefix, expected_file_format)

    students = []
    for student in file:
        new_student = student["Full Name"].split(",")
        new_student.append(student["House"])
        students.append(new_student)

    students.pop(0)

    # for student in students:
    #     print(student)

    student_dicts = []


    for ln, fn, h in students:
        student = {}
        student["first"] = fn.strip()
        student["last"] = ln.strip()
        student["house"] = h.strip()
        student_dicts.append(student)

    # for student in student_dicts:
    #     print(student)

    with open(f"{output_file_name_prefix}.{expected_file_format}", 'w', newline='') as csvfile:
        fieldnames = ["first", "last", "house"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for student in student_dicts:
            writer.writerow(student)

    # student = {"First Name" :"First Name", "Last Name" : "Last Name", "House" : "House"}
    # student_dicts.insert(0, student)
    # print(Tablulate_File(student_dicts))


def Tablulate_File(file, my_headers='firstrow', my_tablefmt='grid'):
    return tabulate(file, headers=my_headers, tablefmt=my_tablefmt)

def Load_File_To_Memory(file_name_prefix, expected_file_format):

    students = {}

    try:
        with open(f'{file_name_prefix}.{expected_file_format}') as file:
            reader = csv.DictReader(file, fieldnames = ["Full Name", "House"])
            students = [dict(d) for d in reader]


    except FileNotFoundError:
        sys.exit("File not Found")

    return students




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
        sys.exit(f"Not a {expected_file_format.capitalize()} file")
    elif file_name[1] != expected_file_format:
        sys.exit(f"Not a {expected_file_format.capitalize()} file")

    return file_name[0]

if __name__ == "__main__":
    Main()
