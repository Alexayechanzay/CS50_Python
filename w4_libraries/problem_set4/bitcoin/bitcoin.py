import requests
import sys


try:
    if len(sys.argv) > 1 :
        try:
            if float(sys.argv[1]):
                bitcoin = float(sys.argv[1])
                response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
                response = response.json()
                amount = response["bpi"]["USD"]["rate"]
                price = ''
                for num in amount:
                    if num != ',':
                        price += num
                price = float(price) * bitcoin
                print(f"${price:,.4f}")

        except ValueError:
            sys.exit("Command-line argument is not a number")
    else:
        sys.exit("Missing command-line argument")
except requests.RequestException:
    print('Error')

# 2 errors
# 1. input validation test
# 2. Could not convert string to float
