# Prompt the user to enter the name of an item and remove leading/trailing whitespace
input = input('item: ').strip()

# Define a dictionary that maps fruit names to their calorie counts
fruits = {'apple': 130,
          'avocado': 50,
          'banana': 110,
          'cantaloup': 50,
          'grapefruit': 60,
          'grapes': 90,
          'honeydew Melon': 50,
          'kiwifruit': 90,
          'lemon': 15,
          'lime': 20,
          'nectarine': 60,
          'orange': 80,
          'peach': 60,
          'pear': 100,
          'pineapple': 50,
          'plums': 70,
          'strawberries': 50,
          'sweet cherries': 100,
          'tangerine': 50,
          'watermelon': 80}

# Iterate through the dictionary to find a matching fruit based on the user's input
for fruit, calorie in fruits.items():
    # Check if the user's input contains the fruit name
    if fruit in input.lower():
        # Print the calorie count for the matched fruit
        print(f'Calories: {calorie}')
