# Exchange rates
# 3rd party imports
import requests
import json

response = requests.get('https://api.exchangeratesapi.io/latest')


def handling_error_codes(response):
    # Error handling if the API returns an error
    if response.status_code == 200:
        print('Success!')
    elif response.status_code == 403:
        print("Forbidden, an API key or secret code is needed to access this data ")
    else:
        print('Error, response code is: {}'.format(response.status_code))


# Query the api for exchange rates for the period 01/01/2018 - 01/01/2021


if __name__ == "__main__":
    handling_error_codes(response)
