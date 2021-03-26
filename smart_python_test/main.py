# Query API
import requests
# import json
response = requests.get('https://api.opencorporates.com/v0.4/companies/secarch?q=smart')
print(response)

# # Get list of companies with word "smart" in their name
# if __name__ == '__main__':
#     print_hi('PyCharm')
