from emoji import emojize

# prompt user for input
text = input('Input: ')

# emojize user's input
text = emojize(text, language = 'alias')

# print output
print(f'Output: {text}')
