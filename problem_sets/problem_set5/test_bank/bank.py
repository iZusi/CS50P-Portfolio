def main():
    # get user input
    greeting = input("Greeting: ").strip()

    # call value function and store in a variable
    output = value(greeting)

    # print output
    print(f"${output}")


def value(greeting):
    if "hello" in greeting:
        x = 0
    elif "Hello" in greeting:
        x = 0
    elif "HELLO" in greeting:
        x = 0
    elif "H" in greeting[0]:
        x = 20
    elif "h" in greeting[0]:
        x = 20
    else:
        x = 100

    return x


if __name__ == "__main__":
    main()
