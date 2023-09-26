import sys
import csv
from tabulate import tabulate

def read_csv_file(filename):
    # use a try-except block to check if file exists
    try:
        # create an empty list to store dictionary
        data = []

        with open(filename) as file:
            file = csv.DictReader(file)
            for line in file:
                data.append(line)
        return data
    except FileNotFoundError:
        sys.exit("File does not exist")

def main():
    # check if one argument was passed
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    # check if more than one argument was passed
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    filename = sys.argv[1]

    # check if file is a .csv file
    if not filename.endswith('.csv'):
        sys.exit("Not a CSV file")

    # call 'read_csv_file' function and store in a variable
    table_data = read_csv_file(filename)

    # check if csv file has data in it
    if not table_data:
        sys.exit("No data found in the CSV file")

    # Format the table using tabulate with the grid format
    table = tabulate(table_data, headers="keys", tablefmt="grid")
    print(table)

if __name__ == "__main__":
    main()
