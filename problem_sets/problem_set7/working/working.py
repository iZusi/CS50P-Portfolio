import re
import sys

def convert(time):
    try:
        # define the regex pattern for the time
        time_pattern = r"^(\d+)(?::(\d+))? (\w+) to (\d+)(?::(\d+))? (\w+)$"

        # use re.search to find the matching input
        matches = re.search(time_pattern, time)

        if not matches:
            raise ValueError("ValueError")

        # Extract the matched times
        hr1 = int(matches.group(1))
        min1 = int(matches.group(2) or "0")
        am_pm1 = matches.group(3).lower()
        hr2 = int(matches.group(4))
        min2 = int(matches.group(5) or "0")
        am_pm2 = matches.group(6).lower()

        # Check for valid time values
        if not (0 <= hr1 <= 12 and 0 <= min1 <= 59 and 0 <= hr2 <= 12 and 0 <= min2 <= 59):
            raise ValueError("ValueError")

        # call the convert_to_24 function to convert the time to 24-hour format
        t1_24 = convert_to_24(hr1, min1, am_pm1)
        t2_24 = convert_to_24(hr2, min2, am_pm2)

        return t1_24, t2_24
    except ValueError:
        sys.exit("ValueError")

def convert_to_24(hour, min, am_pm):
    # Convert AM/PM time to 24-hour format
    if (am_pm == 'pm') and (hour != 12):
        hour += 12
    elif (am_pm == 'am') and (hour == 12):
        hour = 0

    return f"{hour:02}:{min:02}"

def main():
    time = input("Time: ").strip()

    # call convert function to convert user time input and store in a variable
    convert_time = convert(time)

    if convert_time:
        t1_24, t2_24 = convert_time
        print(f"{t1_24} to {t2_24}")

if __name__ == "__main__":
    main()
