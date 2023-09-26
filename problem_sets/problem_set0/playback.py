# Prompt the user for input and store it in the 'prompt' variable
prompt = input('').strip()

# Replace all spaces in the input with '...' using the .replace() method
prompt = prompt.replace(' ', '...')

# Print the modified 'prompt'
print(prompt)
