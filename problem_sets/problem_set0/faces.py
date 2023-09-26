# Define a function 'convert' to replace emoticons with emojis
def convert(msg):
    # Replace ':)' with a smiling emoji '🙂'
    msg = msg.replace(':)', '🙂')
    
    # Replace ':(' with a frowning emoji '🙁'
    msg = msg.replace(':(', '🙁')

    # Print the modified message with emojis
    print(msg)

# Define the 'main' function as the entry point of the program
def main():
    # Prompt the user for input and store it in 'prompt'
    prompt = input('')
    
    # Call the 'convert' function to process and print the input
    convert(prompt)

# Call the 'main' function to start the program
main()
