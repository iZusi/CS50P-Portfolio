import sys
import requests

try:
    # Check if a command-line argument is provided
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")  # Exit with an error message if no argument is provided

    # Get the number of Bitcoins from the command-line argument and convert it to a float
    n_bitcoins = float(sys.argv[1])

    # Define the API link for retrieving Bitcoin exchange rates and make a GET request
    link = "https://api.coindesk.com/v1/bpi/currentprice.json"
    r = requests.get(link)

    # Get the JSON content from the response and store it in a variable
    data = r.json()

    # Get the floating-point value of the current Bitcoin rate in USD from the JSON data
    current_price = data["bpi"]["USD"]["rate_float"]

    # Calculate the total cost by multiplying the number of Bitcoins with the current rate
    total = n_bitcoins * current_price

    # Print the total cost with proper formatting
    print(f"${total:,.4f}")

except (ValueError, requests.RequestException):
    sys.exit("Command-line argument is not a number")
