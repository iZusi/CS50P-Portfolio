import sys
import requests


try:
    # check if command-line argument is empty
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")

    # get the number of Bitcoins from the command-line argument
    n_bitcoins = float(sys.argv[1])

    # store link in a variable and make a request
    link = "https://api.coindesk.com/v1/bpi/currentprice.json"
    r = requests.get(link)

    # get the json content and store in a variable
    data = r.json()

    # get floating-point value current Bitcoin rate in USD
    current_price = data["bpi"]["USD"]["rate_float"]

    # calculate the total cost
    total = n_bitcoins * current_price

    # print result
    print(f"${total:,.4f}")

except (ValueError, requests.RequestException):
    sys.exit("Command-line argument is not a number")
