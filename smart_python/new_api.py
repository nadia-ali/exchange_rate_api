# 3rd party
import requests
import pandas as pd

# in-built
import json
import sqlite3
from sqlite3 import Error


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
    print(csv_data)
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


def create_table(db_file, sql):
    # Create table to store data.
    connection = db_connection(db_file)
    cur = connection.cursor()
    sql = """ CREATE TABLE IF NOT EXISTS exchange_rates (
                            date_created varchar PRIMARY KEY
                            currency varchar
                            rate integer); """
    cur.execute(sql)
    connection.commit()
    return None


def insert_data(db_file):
    # Upload CSV to database
    sql = ''' INSERT INTO exchange_rates(date_created,currency,rate)
                  VALUES(?,?,?) '''
    connection = db_connection(db_file)
    csv_file = output_to_csv()
    cur = connection.cursor()
    cur.execute(sql, csv_file)
    connection.commit()

    return None


if __name__ == "__main__":
    handling_error_codes()
    get_rates()
    output_to_csv()
    db_connection("")
    create_table(db_file="", sql="")
    insert_data("")

