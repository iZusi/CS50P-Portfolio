def main():
    plate = input("Enter a vanity plate: ").strip().upper()

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) >= 2 and len(s) <= 6:
        if s[0].isalpha() and s[1].isalpha():
            if s[-1].isdigit() and s[0] != '0':
                if all(char.isalpha() or char.isdigit() for char in s):
                    return True

    return False


if __name__ == "__main__":
    main()
