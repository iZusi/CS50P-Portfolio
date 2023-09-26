import sys
import os
from PIL import Image, ImageOps

def overlay_shirt(input_path, output_path):
    try:
        # Open input and shirt images
        input_image = Image.open(input_path)
        shirt_image = Image.open("shirt.png")

        # Resize and crop input image to match shirt size
        resized_input = ImageOps.fit(input_image, shirt_image.size)

        # Overlay the shirt on the resized input image
        resized_input.paste(shirt_image, shirt_image)

        # Save the resulting image
        resized_input.save(output_path)

    except FileNotFoundError:
        sys.exit("File not found")

def main():
    # check if two arguments were passed
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    # check if more than two arguments were passed
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    input_path, output_path = sys.argv[1], sys.argv[2]

    # Check for valid file extensions
    valid_extensions = {'.jpg', '.jpeg', '.png'}
    input_extension = os.path.splitext(input_path)[1].lower()
    output_extension = os.path.splitext(output_path)[1].lower()

    if not (input_extension in valid_extensions and output_extension in valid_extensions):
        sys.exit("Invalid input")

    # Check if input and output have the same file extensions
    if input_extension != output_extension:
        sys.exit("Input and output files must have the same extensions")

    # Call the overlay_shirt function
    overlay_shirt(input_path, output_path)

if __name__ == "__main__":
    main()
