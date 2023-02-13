import sys
import requests


def get_btc_price():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        data = response.json()
        return data["bpi"]["USD"]["rate_float"]
    except requests.RequestException:
        sys.exit()


def main():
    try:
        n = float(sys.argv[1])
    except IndexError:
        sys.exit("Missing command-line argument")
    except ValueError:
        sys.exit("Command-line argument is not a number")
    print(f"${n * get_btc_price():,.4f}")


if __name__ == "__main__":
    main()
