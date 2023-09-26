import re


def validate(ip):
    # Define the regex pattern for a valid IP address
    ip_pattern = r"^(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)$"

    # Check if the input fully matches the pattern
    return bool(re.fullmatch(ip_pattern, ip))

def main():
    # Get user input for the IP address
    ip = input("IPv4 Address: ").strip()

    # Validate IP address and print result
    if validate(ip):
        print("True")
    else:
        print("False")

if __name__ == "__main__":
    main()
