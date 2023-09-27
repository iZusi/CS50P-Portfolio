### Problem Set 4 - Week 4 (Libraries)

- [emojize.py](./emojize.py):  This code imports the 'emojize' function from the 'emoji' module, prompts the user for input, emojizes the input by replacing emoji aliases with actual emojis, and then prints the emojized output. The 'alias' language parameter specifies that emoji aliases in the input should be interpreted.

- [figlet.py](./figlet.py):  This code checks command-line arguments to select a font from the Figlet library and use it to format user input text. It supports random font selection, manual font selection using command-line arguments, and handles various error cases for invalid usage.
  
- [adieu.py](./adieu.py):   Here, my code collects names from the user until ctrl-d is used to exit the program and then formats and bids adieu to the names based on the number of names entered. The comments provide clarity on the program's purpose and how it handles different cases for naming farewell.
  
- [game.py](./game.py):  Implemented a guessing game where the user selects a level, guesses a random number within that level, and receives feedback on their guesses. The game can be restarted by entering a new level or exiting the program. The code uses error handling to handle invalid inputs and negative numbers.
  
- [professor.py](./professor.py):  This program prompts the user to select a level (1, 2, or 3) and generates ten addition problems with two-digit non-negative integers. Users must solve each problem; incorrect or non-numeric answers receive up to three attempts before revealing the correct solution. The program then calculates and displays the user's score, representing the number of correctly answered problems out of 10.

- [bitcoin.py](./bitcoin.py):  This code takes a user-provided amount of Bitcoins, fetches the current Bitcoin-to-USD exchange rate from the CoinDesk API, and calculates the equivalent amount in USD. It ensures the presence of a valid command-line argument, converts it to USD using the fetched rate, and prints the result. If there are errors in the input or API request, it exits with an error message.
