# 3rd party
import requests
# in-built
import json

api_url = 'https://api.exchangeratesapi.io/latest'
response = requests.get(api_url)


def handling_error_codes(r):
    # Error handling if the API returns an error
    if r.status_code == 200:
        print('Success!')
    elif r.status_code == 403:
        print("Forbidden, an API key or secret code is needed to access this data")
    elif r.status_code == 429:
        print("Reached API requests limit")
    else:
        print('Error, response code is: {}'.format(r.status_code))


def query_api():
    # Querying the api for exchange rates for the period 01/01/2018 - 01/01/2021
    exchange_rates = requests.get('https://api.exchangeratesapi.io/'
                                  'history?start_at=2018-01-01&end_at=2021-01-01&base=DKK')
    data = exchange_rates.text
    parsed = json.loads(data)
    return parsed


def exchange_currency():
    # Extract exchange and conversion rates
    parsed_data = query_api()
    rates = parsed_data["rates"]
    for key, val in rates.items():
        print("Date: ", key, "GBP Rate: ", val['GBP'])
        print("Date: ", key, "USD Rate: ", val['USD'])
        print("Date: ", key, "EUR Rate: ", val['EUR'])

    # Extract conversion rates to all currencies


# def output_to_csv():
    # Writing data to CSV file


# def csv_to_db():
    # Upload CSV to database


if __name__ == "__main__":
    handling_error_codes(response)
    query_api()
    exchange_currency()
    # conversion_rates()
