import requests
import json
import pprint

f1_api = "http://ergast.com/api/f1"
news_url = 'https://newsapi.org/v2/everything?'
news_key = 'c78ac9726f714b79b3798843898a7400'

# Valid Options: 
# year: see getF1Season options
# race: any valid 1 or 2 digit race number during the selected season
def getF1Race(year="current", race="next"):
	f1_race = f1_api+year+"/"+race+".json"
	result = requests.get(f1_race)
	return result

# Valid Options
# 'current'
# Any 4 digit year number during which there was an F1 season, from 1950 to 2020
def getF1Season(year="current"):
	f1_season = f1_api+year+".json"
	result = requests.get(f1_season)
	return result

def getWeather(city='London'):
	key = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=2e535070ac9219e3c58f19ac7227c197&'.format(city)
	result = requests.get(key)
	return result

def getNews(url, pageSize=20,apiKey):
	# Specify the query and number of returns
	parameters = {
    		'q': 'F1', # query phrase
    		'pageSize': 20,  # maximum is 100
    		'apiKey': secret # your own API key
	}

	# Make the request
	response = requests.get(url, params=parameters)

	# Convert to JSON
	#response_json = response.json()
	
	return response
    
def menu():
	print("Please select which motorsport you would like:")
	msport = input("Choose from:\nF1)

	motorsports = ['F1', 'f1']

	while msport not in motorsports:
	    print("please choose a valid option")
	    msport = input()

	print("Which year?")
	year = input()

	print("Which race would you like?")
	race = input()
	
	


