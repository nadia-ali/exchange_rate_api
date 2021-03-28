# exchange_rate_api

In this exercise, you will need to query an api (https://exchangeratesapi.io/). You will need to:

* Query the api for exchange rates for the period 01/01/2018 - 01/01/2021
* For each day, retrieve the exchange rates for UK Sterling (GBP), US Dollars (USD) and
Euros (EUR) and the conversion rates to all currencies provided by the API
* Output the collected data to a CSV file
* Upload the CSV file to a database (any local database will be sufficient, e.g. SQLLite,
MySQL, etc.)

Additional considerations

Please include consideration for the following:

* Automated unit tests
* Error handling if the API returns error codes
* Handling of API rate limiting
* How to handle API keys/secrets if the API were to require such things
* Consideration for how the code would perform with much higher volumes of data (e.g.
100,000 company records)

Files:
* new_api.py = Main Python Script
* tests.py = Test for code 

Note:
* Some strings are empty as they should contain file paths to local files 
