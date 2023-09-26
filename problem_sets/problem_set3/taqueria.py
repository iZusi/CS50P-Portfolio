# We're gonna be implementing a program that prompts the user to
# place an order

# using a dictionary, create a menu of entrees along with the prices
menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
}

# create and initialize the variable for the total prices
total = 0

# print exit instruction for user
print("\nUse 'ctrl-d' to exit the program\n")

# create a while loop
while True:
    try:
        # prompt the user for an input
        item = input('Item: ').title().strip()

        # interate through the menu using a for loop
        for entree, price in menu.items():
            if item == entree:
                if total >= 0:
                    total += price
                    print(f'Total: ${total}0')
    except EOFError:
        print('\nBye')
        break
    except KeyError:
        pass
