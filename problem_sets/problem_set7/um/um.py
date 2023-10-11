import re

def count(um):
    # Find all non-overlapping matches of "um" in the input using re.findall
    matches = re.findall(r"\bum\b", um, re.IGNORECASE)

    # Count the number of matches
    count = len(matches)

    return count

def main():
    # Get user's input
    um = input("Input: ").strip()

    # Call the 'count' function
    count_um = count(um)

    # Display result
    print(count_um)

if __name__ == "__main__":
    main()
