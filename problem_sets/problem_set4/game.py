# Creating a guessing game

import random


while True:
    try:
        # prompt user for input
        n = int(input("Level: "))

        if n < 0:
            continue
        else:
            # generate a random number between 1 and n
            output = random.randint(1, n)
    except ValueError:
        continue

    while True:
        try:
            # prompt user again for another input
            guess = int(input("Guess: "))

            if guess < 0:
                continue
            elif guess < output:
                print("Too small!")
                continue
            elif guess > output:
                print("Too large!")
                continue
            elif guess == output:
                print("Just right!")
                break
        except ValueError:
            pass
    break
