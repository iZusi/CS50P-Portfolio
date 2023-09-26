# Coke Machine

# Initialize the amount due for the coke
amount = 50
print(f'Amount Due: {amount}')

# Initialize the variable to keep track of the coins inserted by the user
insert_coin = int(0)

# Define the list of coin denominations accepted by the machine
denom = [5, 10, 25]

while True:
    # Prompt the user to insert a coin and convert their input to an integer
    insert_coin = int(input('Insert Coin: '))

    # Check if the inserted coin is a valid denomination
    if insert_coin in denom:
        # Check if there is still an amount due
        if amount > 0:
            # Subtract the inserted coin from the amount due
            amount -= insert_coin

            # Check if the amount due is now zero or negative (indicating change owed)
            if amount <= 0:
                amount = -1 * amount  # Convert the negative amount to positive for change owed
                print(f'Change Owed: {amount}')
                break

            # Print the updated amount due
            print(f'Amount Due: {amount}')
    else:
        # If the inserted coin is not a valid denomination, print the current amount due
        print(f'Amount Due: {amount}')
