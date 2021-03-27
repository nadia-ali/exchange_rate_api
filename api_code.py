# 3rd party
import requests
import pandas as pd

# in-built
import json
import sqlite3
from sqlite3 import Error
import csv


def handling_error_codes():
    # Error handling if the API returns an error
    api_url = 'https://api.exchangeratesapi.io/latest'
    r = requests.get(api_url)
    if r.status_code == 200:
        print('Success!')
    elif r.status_code == 403:
        print("Forbidden, an API key or secret code is needed to access this data")
    elif r.status_code == 429:
        print("Reached API requests limit")
    else:
        print('Error, response code is: {}'.format(r.status_code))


def get_rates():
    # Querying the api for specific exchange rates for the period 01/01/2018 - 01/01/2021
    rates = requests.get("https://api.exchangeratesapi.io/"
                         "history?start_at=2018-01-01&end_at=2021-01-01&symbols=GBP,USD,EUR&base=DKK")
    data = rates.text
    parsed = json.loads(data)
    parsed_rates = parsed["rates"]
    return parsed_rates


def output_to_csv():
    # Writing data to CSV file
    csv_data = get_rates()
    data_frame = pd.DataFrame(csv_data)
    csv_file = data_frame.to_csv('./rates.csv')
    return csv_file


# def csv_to_db():
    # Upload CSV to database


if __name__ == "__main__":
    handling_error_codes()
    get_rates()
    output_to_csv()
    csv_to_db()

