import sys

def Main():

    expected_command_lines_size = 1
    Validate_Command_Line_Size(expected_command_lines_size + 1)

    expected_file_format = 'py'
    file_name = sys.argv[1].split(".")
    file_name_prefix = Validate_File_Format(expected_file_format, file_name)

    file_lines = Load_File_To_Memory(file_name_prefix, expected_file_format)

    file_lines = Remove_Blank_Lines(file_lines)
    file_lines = Remove_Comment_Lines(file_lines)

    print(Count_Lines(file_lines))

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

    lines = []

    try:
        with open(f'{file_name_prefix}.{expected_file_format}') as file:
            for line in file:
                lines.append(line.rstrip())

    except FileNotFoundError:
        sys.exit("File not Found")

    return lines

# potentially broken
def Remove_Blank_Lines(file_lines):

    lines = []

    for value in file_lines:
        if not value.lstrip():
            pass
        else:
            lines.append(value)

    return lines

# potentially broken
def Remove_Comment_Lines(file_lines):

    lines = []

    for value in file_lines:
        if value.strip().startswith("#"):
            pass
        else:
            lines.append(value)

    return lines

def Count_Lines(file_lines):
    return len(file_lines)


if __name__ == "__main__":
    Main()
