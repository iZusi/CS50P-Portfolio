from emoji import emojize

# Prompt the user for input and store it in a variable
text = input('Input: ')

# Emojize the user's input using the 'emojize' function
# The 'language' parameter is set to 'alias' to interpret emoji aliases in the input
text = emojize(text, language='alias')

# Print the emojized output, which replaces emoji aliases with actual emojis
print(f'Output: {text}')
