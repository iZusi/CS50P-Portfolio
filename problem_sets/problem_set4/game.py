# Creating a guessing game

# Import the 'random' module for generating random numbers
import random

# Start an infinite loop to allow the game to restart
while True:
    try:
        # Prompt the user for the game level and convert it to an integer
        n = int(input("Level: "))

        # Check if the user entered a negative number and continue the loop if so
        if n < 0:
            continue
        else:
            # Generate a random number between 1 and n (inclusive)
            output = random.randint(1, n)
    except ValueError:
        # Handle non-integer inputs gracefully and continue the loop
        continue

    # Start an inner loop for the guessing game
    while True:
        try:
            # Prompt the user to guess the number and convert their input to an integer
            guess = int(input("Guess: "))

            # Check if the user entered a negative number and continue the loop if so
            if guess < 0:
                continue
            # Check if the guess is smaller than the random number
            elif guess < output:
                print("Too small!")
                continue
            # Check if the guess is larger than the random number
            elif guess > output:
                print("Too large!")
                continue
            # Check if the guess is equal to the random number, indicating a correct guess
            elif guess == output:
                print("Just right!")
                break  # Exit the inner loop when the guess is correct
        except ValueError:
            # Handle non-integer inputs gracefully and continue the loop
            pass

    # Exit the outer loop to end the game
    break
