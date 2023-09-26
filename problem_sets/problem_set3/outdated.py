# Let's implement a program that asks for a date in the MM/DD/YYYY format
# and returns the output in the YYYY/MM/DD format

# Create a list of all the months in a year
month = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

# Start list index from 1 using the enumerate() function
month = enumerate(month, 1)

# Create an infinite loop to repeatedly prompt the user for input
while True:
    try:
        # Prompt the user for a date
        date = input('Date: ').strip().title()

        if '/' in date:
            # Split and store input with the '/' delimiter
            mm, dd, yyyy = date.split('/')
            mm, dd, yyyy = int(mm), int(dd), int(yyyy)
            if dd <= 31 and mm <= 12:
                for m in month:
                    if mm in m[:]:
                        # Print the date in the YYYY/MM/DD format
                        print(f'{yyyy}-{mm:02}-{dd:02}')
                break
        elif ',' in date:
            # Split and store input with the ' ' delimiter
            mm, dd, yyyy = date.split(' ')
            dd = dd.replace(',', '')  # Remove ',' from dd
            dd, yyyy = int(dd), int(yyyy)  # Convert dd & yyyy to int
            if dd <= 31 and dd != '':
                for m in month:
                    if mm in m:
                        # Print the date in the YYYY/MM/DD format
                        print(f'{yyyy}-{m[0]:02}-{dd:02}')
                break
    except ValueError:
        pass  # Handle exceptions (ValueError) and continue the loop if invalid input
