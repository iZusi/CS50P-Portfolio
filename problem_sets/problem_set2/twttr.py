# Here we'll implement a program that removes all vowels from our input

def main():
    # Get user input and remove leading/trailing whitespace
    word = input("Input: ").strip()

    # Call the shorten() function and store the result in a variable
    output = shorten(word)

    # Print the output
    print(f"Output: {output}")

# Define the shorten() function, which removes vowels from a given word
def shorten(word):
    # Create a list of all vowels
    vowels = ['a', 'e', 'i', 'o', 'u']

    # Iterate through the list of vowels
    for vowel in vowels:
        # Replace both lowercase and uppercase occurrences of the vowel with an empty string
        word = word.replace(vowel.lower(), '')
        word = word.replace(vowel.upper(), '')

    # Return the word with vowels removed
    return word

if __name__ == "__main__":
    main()
