import sys
import requests

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    data = response.json()
    current_price = data["bpi"]["USD"]["rate_float"]
except requests.RequestException:
    sys.exit()


try:
    n = float(sys.argv[1])
except IndexError:
    sys.exit("Missing command-line argument")
except ValueError:
    sys.exit("Command-line argument is not a number")
print(f"${n * current_price:,.4f}")
