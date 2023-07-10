import sys
import requests
import json

def main():

    bitcoin_count = float(sys.argv[1])

    try:
        bitcoin_information = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
        bitcoin_value = bitcoin_information["bpi"]["USD"]["rate_float"]
        users_worth = bitcoin_count * bitcoin_value
        print(f'${users_worth:,.4f}')

    except requests.RequestException:
        print("Something went wrong with the API request")
        print(requests.RequestException)




if __name__ == "__main__":

    if len(sys.argv) == 1:
        exit("Missing command-line argument")
    elif sys.argv[1].isalpha():
        exit("Command-line argument is not a number")

    main()
