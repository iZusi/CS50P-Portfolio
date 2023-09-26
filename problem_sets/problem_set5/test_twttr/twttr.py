# Here we'll implement a program that removes all vowels from our input

# define main() function
def main():
    # get user input
    word = input("Input: ").strip()

    # call shorten function and store in a variable
    output = shorten(word)

    # print output
    print(f"Output: {output}")

# define function to remove vowels
def shorten(word):
    # create a list of all vowels
    vowels = ['a', 'e', 'i', 'o', 'u']

    for vowel in vowels:
        word = word.replace(vowel.lower(), '')
        word = word.replace(vowel.upper(), '')

    return word

if __name__ == "__main__":
    main()
