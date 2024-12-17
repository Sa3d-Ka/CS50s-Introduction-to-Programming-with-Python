import sys
import requests
import json

# Ensure a command-line argument is provided
if len(sys.argv) != 2:
    print("Missing command-line argument")
    sys.exit(1)

try:
    # Get the number of Bitcoins from the command-line argument
    n = float(sys.argv[1])
except ValueError:
    print("Command-line argument is not a number")
    sys.exit(1)

# Fetch Bitcoin price data
response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
data = response.json()

# Extract the current price of Bitcoin in USD
rate = float(data["bpi"]["USD"]["rate"].replace(",", ""))  # Remove commas for conversion

# Calculate the total cost for the given number of Bitcoins
total_cost = n * rate

# Print the result formatted to 4 decimal places
print(f"${total_cost:,.4f}")