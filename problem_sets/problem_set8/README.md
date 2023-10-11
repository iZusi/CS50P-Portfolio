### Problem Set 8 - Week 8 (Object-oriented Programming)

- [seasons.py](./seasons/seasons.py):  This module validates and converts a user's input for their date of birth in the format "YYYY-MM-DD." It uses regular expressions to check the input's format. If the input is valid, it calculates the user's age in minutes by comparing the birthdate to the current date and then converts this age into words using the `inflect` library.
  
- [test_seasons.py](./seasons/test_seasons.py):  This code conducts two concise tests using the ``pytest` framework for a function named `get_birthday` from the `seasons` module. The first test verifies that the function correctly converts "2000-01-01" to its equivalent age in minutes, expressed in words. The second test checks if the function raises a "SystemExit" exception when provided with an invalid date format like '01-01-2021.' These tests ensure the proper functionality of the `get_birthday` function and its handling of invalid inputs.