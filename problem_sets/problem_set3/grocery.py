# Let's create a program that prompts the user for their list of items in a grocery list

# create an empty dictionary to store items. This will be our grocery list
grocery_list = {}

# create a while loop
while True:
    try:
        # prompt the user for a food item
        item = input('').strip().upper()

        if item in grocery_list:
            grocery_list[item] = grocery_list.get(item) + 1
        else:
            grocery_list[item] = 1
    except EOFError:
        for name, num in sorted(grocery_list.items()):      #sort dictionary alphabetically
            print(f'{num} {name}')
        break
