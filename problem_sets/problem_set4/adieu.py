# Program Description:
# This program prompts the user for names, one per line, until the user inputs Ctrl-D.
# It assumes that the user will input at least one name and then bids adieu to those names.
# The program separates two names with one "and," three names with two commas and one "and,"
# and n names with n - 1 commas and one "and."

# Create an empty list to store names
lst = []

# Continuously prompt the user until they enter Ctrl-D (EOFError) to exit the program
while True:
    try:
        # Get the user's input for a name, titlecase it, and remove leading/trailing whitespace
        name = input('Name: ').title().strip()

        # Add the user's input to the list of names
        lst.append(name)

    except EOFError:
        if len(lst) == 1:
            # If there is only one name, bid adieu to that name
            print(f'\nAdieu, adieu, to {lst[0]}')
            break
        elif len(lst) == 2:
            # If there are two names, bid adieu to both with "and" between them
            print(f'\nAdieu, adieu, to {lst[0]} and {lst[1]}')
            break
        else:
            # If there are more than two names, format and bid adieu to all of them
            # using commas and "and" as appropriate
            print(f'\nAdieu, adieu, to ' + ', '.join(lst[:-1]) + f', and {lst[-1]}')
            break
