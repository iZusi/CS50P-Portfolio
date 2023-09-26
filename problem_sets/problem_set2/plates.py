def main():
    # Prompt the user to input a license plate and remove leading/trailing whitespace, then convert to uppercase
    plate = input("Plate: ").strip().upper()

    # Check if the entered license plate is valid using the is_valid function
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

# Define the is_valid function to check if a license plate is valid
def is_valid(s):
    # Check the length of the string (between 2 and 6 characters)
    if len(s) >= 2 and len(s) <= 6:
        # Check if the first two characters are alphabetical
        if s[0].isalpha() and s[1].isalpha():
            # Check if the last character is a digit and the first character is not '0'
            if s[-1].isdigit() and s[0] != '0':
                # Check if all characters in the string are either alphabetical or digits
                if all(char.isalpha() or char.isdigit() for char in s):
                    return True  # The license plate is valid if all conditions are met

    return False  # The license plate is invalid if any of the conditions fail

if __name__ == "__main__":
    main()
