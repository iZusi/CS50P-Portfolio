# Here, we want to implement a program that prompts the user for names, one per line,
# until the user inputs ctrl-d. We'll assume that the user will input at least one name.
# Then bid adieu to those names, separating two names with one "and",
# three names with two commas and one "and", and n names with n - 1 commas and one "and".


# create an empty list to store names
lst = []

# we need to continually prompt the user until they enter ctrl-d to exit the program.
while True:
    try:
        # get user's input
        name = input('Name: ').title().strip()

        # add user's input to list
        lst.append(name)

    except EOFError:
        if len(lst) == 1:
            print(f'\nAdieu, adieu, to {lst[0]}')
            break
        elif len(lst) == 2:
            print(f'\nAdieu, adieu, to {lst[0]} and {lst[1]}')
            break
        else:
            # concatenate and print elements from the list into a single string, separated by a specified delimiter.
            print(f'\nAdieu, adieu, to ' + ', '.join(lst[:-1]) + f', and {lst[-1]}')
            break
