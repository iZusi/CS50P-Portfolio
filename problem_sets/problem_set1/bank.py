# Prompt the user for a greeting and convert it to lowercase with leading/trailing whitespace removed
greeting = input('Greeting: ').lower().strip()

# Check if 'hello' is present anywhere in the greeting
if 'hello' in greeting:
    # If 'hello' is found, print '$0'
    print('$0')
elif 'h' in greeting[0]:
    # If the first character of the greeting is 'h', print '$20'
    print('$20')
else:
    # If none of the above conditions are met, print '$100'
    print('$100')
