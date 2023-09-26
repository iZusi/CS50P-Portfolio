# get user input
prompt = input('camelCase: ').strip()

prompt = prompt.replace('name', 'name')
prompt = prompt.replace('firstName', 'first_name')
prompt = prompt.replace('preferredFirstName', 'preferred_first_name')

print(f'snake_case: {prompt}')
