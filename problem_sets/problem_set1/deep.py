# Prompt the user with a question and store their response in 'prompt'
prompt = input('What is the answer to the Great Question of Life, the Universe, and Everything? ').lower().strip()

# Use the match statement to perform pattern matching on 'prompt'
match prompt:
    # Check for specific cases where the user's input matches the expected answers
    case '42'|'forty two'|'forty-two':
        # If the input matches '42', 'forty two', or 'forty-two', print 'Yes'
        print('Yes')
    case _:
        # If the input doesn't match any of the specified cases, print 'No'
        print('No')
