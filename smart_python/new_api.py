# 3rd party
import requests
import pandas as pd

# in-built
import json
import sqlite3
from sqlite3 import Error
# import csv


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


def db_connection(db_file):
    """ create a database connection to the SQLite database
        :param db_file: database file
        :return: Connection object or None """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def csv_to_db(db_file):
    # Upload CSV to database
    connection = db_connection(db_file)
    cur = connection.cursor()
    cur.execute('''CREATE TABLE rates
                   (date text, currency text, rate text)''')
    connection.commit()
    connection.close()


def create_table(create_table_sql=None):
    # create database table which will store data
    try:
        c = db_connection.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

# 
# def insert_data():
#     Insert csv file data to table within database

# def query_api():
#
#     exchange_rates = requests.get('https://api.exchangeratesapi.io/'
#                                   'history?start_at=2018-01-01&end_at=2021-01-01&base=DKK')
#     data = exchange_rates.text
#     parsed = json.loads(data)
#     return parsed


# def exchange_currency():
#     # Extract exchange and conversion rates
#     parsed_data = query_api()
#     rates = parsed_data["rates"]
#     data = ""
#     for key, val in rates.items():
#         print("Date: ", key, "GBP Rate: ", val['GBP'])
#         print("Date: ", key, "USD Rate: ", val['USD'])
#         print("Date: ", key, "EUR Rate: ", val['EUR'])


if __name__ == "__main__":
    handling_error_codes()
    # query_api()
    # exchange_currency()
    get_rates()
    output_to_csv()
    db_connection("")
    csv_to_db("")

