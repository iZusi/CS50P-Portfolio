# Define the main function, which is the entry point of the program
def main():
    # Prompt the user for input and remove any leading/trailing whitespace
    prompt = input('What is the time? ').strip()

    # Call the convert function with the user's input
    convert(prompt)

def convert(time):
    # Split the time string into hours and minutes using the colon (:) as a separator
    hours, minutes = time.split(':')
    
    # Convert the hours and minutes to floating-point numbers
    hours = float(hours)
    minutes = float(minutes)
    
    # Calculate the time in hours as a floating-point number, considering the minutes
    time = hours + (minutes / 60)

    # Check if the calculated time falls within specific ranges and print corresponding messages
    if time >= 7.0 and time <= 8.0:
        print('breakfast time')
    elif time >= 12.0 and time <= 13.0:
        print('lunch time')
    elif time >= 18.0 and time <= 19.0:
        print('dinner time')

    return time

# Check if this script is being run as the main program
if __name__ == "__main__":
    # If so, call the main function to start the program
    main()
