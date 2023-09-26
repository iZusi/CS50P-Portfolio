import random

def main():
    # Get the user-selected level for the game
    level = get_level()
    
    # Initialize the player's score to 0
    score = 0

    # Play 10 rounds of the addition game
    for _ in range(10):
        # Generate two random integers based on the selected level
        x = generate_integer(level)
        y = generate_integer(level)
        
        # Calculate the correct result
        result = x + y

        # Allow the player three attempts to provide the correct answer
        tries = 0
        while tries < 3:
            answer = input(f"{x} + {y} = ")
            
            # Check if the input is a valid integer
            if answer.isdigit():
                answer = int(answer)
                
                # Check if the answer is correct
                if answer == result:
                    score += 1  # Increase the player's score if the answer is correct
                    break
                else:
                    print("EEE")  # Notify the player of an incorrect answer
                    tries += 1
            else:
                print("EEE")  # Notify the player of an incorrect answer format
                tries += 1

        # If the player has used all three attempts, reveal the correct answer
        if tries == 3:
            print("EEE")
            print(f"{x} + {y} = {result}")

    # Display the player's final score
    print(f"Score: {score}")

# Function to get the game level from the user
def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in (1, 2, 3):
                return level  # Return the selected level if it's valid (1, 2, or 3)
        except ValueError:
            pass

# Function to generate random integers based on the game level
def generate_integer(level):
    if level == 1:
        max_num = 10 ** level - 1
        value = random.randint(0, max_num)
    else:
        min_num = 10 ** (level - 1)
        max_num = 10 ** level - 1
        value = random.randint(min_num, max_num)
    return value

if __name__ == "__main__":
    main()
