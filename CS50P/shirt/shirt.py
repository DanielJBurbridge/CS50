from PIL import Image
from PIL import ImageOps
import sys

def main():

    expected_command_lines_size = 2
    Validate_Command_Line_Size(expected_command_lines_size + 1)

    expected_file_formats = ['jpg', 'png', 'jpeg']

    input_file_name = sys.argv[1].split(".")
    output_file_name = sys.argv[2].split(".")

    Validate_File_Format(expected_file_formats, input_file_name)
    Validate_File_Format(expected_file_formats, output_file_name)
    Validate_Same_Format(input_file_name, output_file_name)

    input_image = Load_Image(input_file_name[0], input_file_name[1])
    shirt_image = Load_Image("shirt", "png")

    input_image = Maniputlate_Image(input_image, shirt_image.size)
    Overlay_Image(input_image, shirt_image)
    Save_Image(input_image, output_file_name)


def Maniputlate_Image(image, new_size):
    return ImageOps.fit(image, new_size)

def Overlay_Image(image, overlay_image):
    return image.paste(overlay_image, overlay_image)

def Save_Image(image, file_name):
    image.save(f'{file_name[0]}.{file_name[1]}')

def Load_Image(file_prefix, file_suffix):
    return Image.open(f'{file_prefix}.{file_suffix}')

def Validate_Command_Line_Size(x):

    argv = sys.argv
    if len(argv) == x:
        return True
    elif len(argv) < x:
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Too many command-line arguments")


def Validate_File_Format(expected_file_formats, file_name):

    if len(file_name) == 1:
        sys.exit(f"Invalid input")
    elif file_name[1].lower() not in expected_file_formats:
        sys.exit(f"Invalid input")

    return

def Validate_Same_Format(input_file_name, output_file_name):
    if input_file_name[1].lower() != output_file_name[1].lower():
        sys.exit(f"Input and output have different extensions")



if __name__ == "__main__":
    main()