import sys
import csv

def csv_file(input_file, output_file):
    # define header to swap
    swapped_names = "name"

    # open input file for reading
    with open(input_file) as f:
        # create a csv reader object
        reader = csv.DictReader(f)

        # read the header row
        header = reader.fieldnames

        # create an empty list to store dictionary of flipped names
        swapped_data = []

        # iterate through the rows and flip the target header
        for row in reader:
            # get the contents in the target header
            contents = row[swapped_names].split(",")  # Assuming values are separated by commas

            # check if there are at least 2 items to swap
            if len(contents) >= 2:
                # swap the items in the list
                contents[0], contents[1] = contents[1], contents[0]

                # update the column with the swapped contents
                row[swapped_names] = ", ".join(contents).lstrip()  # Join the values with commas and a whitespace

            # append the modified row to the swapped_data list
            swapped_data.append(row)

    # sort input file
    sorted_data = sorted(swapped_data, key=lambda name: name[swapped_names])

    # open output file for writing
    with open(output_file, "a") as f:
        # create a csv writer object
        writer = csv.DictWriter(f, fieldnames=header)

        # write the header row to the output file
        writer.writeheader()

        # write the flipped data to the output file
        writer.writerows(sorted_data)

    return sorted_data

def main():
    # check if two arguments were passed
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    # check if more than two arguments were passed
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    # check if the input file can be read
    try:
        input_file, output_file = sys.argv[1], sys.argv[2]

        # call 'csv_file' function
        csv_file(input_file, output_file)
    except FileNotFoundError:
        sys.exit(f"Could not read {input_file} file")

if __name__ == "__main__":
    main()
