import sys

def count_lines(filename):
    num_lines = 0
    # use a try-except block to check if file exists
    try:
        with open(filename, 'r') as file:
            for line in file:
                stripped_line = line.strip()
                # ignore blank lines and comment lines
                if stripped_line != '' and not stripped_line.startswith('#'):
                    num_lines += 1
    except FileNotFoundError:
        sys.exit("File does not exist")
    return num_lines

def main():
    # check if one argument was passed
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    # check if more than one argument was passed
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    filename = sys.argv[1]

    # check if file is a .py file
    if not filename.endswith('.py'):
        sys.exit("Not a Python file")

    # print output
    num_lines = count_lines(filename)
    print(num_lines)

if __name__ == "__main__":
    main()
