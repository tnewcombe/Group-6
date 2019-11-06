import requests
import json
import pprint

f1_api = "http://ergast.com/api/f1"

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
    
def menu():
	print("Pleach select which motorsport you would like")
	msport = input()

	motorsports = ['F1', 'f1']

	while msport not in motorsports:
	    print("please choose a valid option")
	    msport = input()

	print("Which year?")
	year = input()

	print("Which race would you like?")
	race = input()


