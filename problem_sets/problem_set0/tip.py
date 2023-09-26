def main():
    # Prompt the user for the meal cost and tip percentage, and store them as floats
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    
    # Calculate the tip amount by multiplying the meal cost by the tip percentage
    tip = dollars * percent
    
    # Print the tip amount with two decimal places
    print(f"Leave ${tip:.2f}")

# Define a function to convert a string representing dollars to a float
def dollars_to_float(d):
    # Remove the dollar sign ('$') and convert the string to a float
    d = float(d.replace('$', ''))
    return d

# Define a function to convert a string representing a percentage to a float
def percent_to_float(p):
    # Remove the percentage sign ('%') and convert the string to a float
    p = float(p.replace('%',''))
    # Convert the percentage to a decimal by dividing by 100
    p = p / 100
    return p

# Call the main() function to start the program
main()
