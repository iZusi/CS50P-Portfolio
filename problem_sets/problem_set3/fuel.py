# Create an while loop to repeatedly prompt the user for input
while True:
    try:
        # Prompt the user to input a fraction and store it in the 'fraction' variable
        fraction = input('Fraction: ')
        
        # Split the input by '/' to separate the numerator and denominator
        x, y = fraction.split('/')
        
        # Calculate the percentage as (numerator/denominator) * 100
        z = (int(x) / int(y)) * 100
        
        # Round the percentage to the nearest whole number
        z = round(z)
        
        # Check various conditions based on the rounded percentage value
        if z <= 1:
            print('E')  # Print 'E' if the percentage is less than or equal to 1
            break
        elif z < 99:
            print(f'{z}%')  # Print the percentage if it's less than 99
            break 
        elif z <= 100:
            print('F')  # Print 'F' if the percentage is less than or equal to 100
            break
        else:
            pass  # Do nothing if none of the above conditions are met
    except (ValueError, ZeroDivisionError):
        pass  # Handle exceptions (ValueError for invalid input or ZeroDivisionError for division by zero) and continue the loop
