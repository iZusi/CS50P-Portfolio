import sys
import re
import inflect
from datetime import date

# create regex pattern for the date format (YYYY-MM-DD)
date_pattern = r"^\d{4}-\d{2}-\d{2}$"

# create inflect engine
p = inflect.engine()

def get_birthday(birthdate):
    while True:
        if re.match(date_pattern, birthdate):
            break
        else:
            sys.exit("Invalid date format. Please use YYYY-MM-DD format.")

    # split date into appropriate factions
    year, month, day = birthdate.split("-")

    # convert to integer and get birthday
    year, month, day = int(year), int(month), int(day)
    birthday = date(year, month, day)

    # get current date
    today = date.today()

    # calculate age difference
    age_diff = today - birthday

    # calculate age difference in minutes
    age_in_mins = age_diff.days * 24 * 60

    # convert the age in minutes to words in an American date format
    age_in_words = p.number_to_words(age_in_mins, andword="")

    return age_in_words.capitalize()

def main():
    # get user's data
    birthday = input("Date of Birth (YYYY-MM-DD): ").strip()

    # call get_birthday function to calculate date of birth
    d_o_b = get_birthday(birthday)
    print(f"{d_o_b} minutes")

if __name__ == "__main__":
    main()
