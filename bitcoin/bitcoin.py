# Bitcoin app
# To run program: python {file name} {amount of bitcoin}

"""
Program that uses bitcoin api to give back realtime value of bit coin.
"""

import sys
import json
import requests

def main():

    if len(sys.argv) != 2:
        print("Missing command-line argument")
        sys.exit(1)

    if sys.argv[1].isalpha():
        print("Command-line argument is not a number")
        sys.exit(1)

    try:
        response = requests.get(
            "https://rest.coincap.io/v3/assets?apiKey=25e7df87f412e38795ac691c4fe01b11d306707bdb1145f1b30fdad64090d2a7" 
        )
        response.raise_for_status()
    except requests.RequestException:
        pass

    crypto = response.json()
    # print(crypto)

    result = crypto['data']
    
    for item in result:
        if item["id"].lower() == "bitcoin":
            result = item

    # print(result)

    # Print the json data first to see the variable names used to store the relevent data.
    price_per_bitcoin = result['priceUsd']
    price_per_bitcoin = float(price_per_bitcoin)

    quantity = float(sys.argv[1])

    amount = quantity*price_per_bitcoin
    amount = float(amount)

    print(f"The current price of bitcoin is: ${price_per_bitcoin}")
    print(f"> {quantity} bitcoin,is worth: ${amount:,.4f}")

if __name__ == "__main__":
    main()
