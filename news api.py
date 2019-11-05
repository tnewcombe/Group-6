import pprint
import requests

secret = 'c78ac9726f714b79b3798843898a7400'

url = 'https://newsapi.org/v2/everything?'

# Specify the query and number of returns
parameters = {
    'q': 'F1', # query phrase
    'pageSize': 20,  # maximum is 100
    'apiKey': secret # your own API key
}

# Make the request
response = requests.get(url, params=parameters)

# Convert to JSON
response_json = response.json()

# print JSON
pprint.pprint(response_json)

# create array and store titles of articles
titles = []
for i in response_json['articles']:
    titles.append(i['title'])
    

