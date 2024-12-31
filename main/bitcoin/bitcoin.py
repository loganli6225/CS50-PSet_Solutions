import requests
import sys

if len(sys.argv) < 2:
    sys.exit("Missing command-line argument")
elif len(sys.argv) > 2:
    sys.exit("Too many command line arguments")
else:
    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    organized_response = response.json()
except requests.RequestException:
    sys.exit("Error - Try Again")
else:
     rate = (((organized_response["bpi"])["USD"])["rate_float"])

usd = n * rate
print(f"${usd:,.4f}")
