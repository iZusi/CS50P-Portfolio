# Get user input and prompt for camelCase text
prompt = input('camelCase: ').strip()

# Replace specific camelCase words with their snake_case equivalents
prompt = prompt.replace('name', 'name')
prompt = prompt.replace('firstName', 'first_name')  # Replace 'firstName' with 'first_name'
prompt = prompt.replace('preferredFirstName', 'preferred_first_name')  # Replace 'preferredFirstName' with 'preferred_first_name'

# Print the modified string in snake_case format
print(f'snake_case: {prompt}')
