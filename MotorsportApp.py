import requests
import json
import praw
from pprint import pprint
from datetime import datetime

f1_api = "http://ergast.com/api/f1/"
news_url = 'https://newsapi.org/v2/everything?'
news_key = 'c78ac9726f714b79b3798843898a7400'
#NEW KEYS
f1_key = 'ddpgefjjw8jpvsxtzzrar4tg'
fe_key = 'tghwbk5bbq9xdhh4ffc6nm2q'
nascar_key = 'b9yp48fazmd4j7dsj3z6fkjr'
indy_key = 'rantz54umfy25grmk89vt7r5'
motogp_key = '6hu6q2j774j8k7nvpkntunq6'

#REDDIT KEYS
reddit = praw.Reddit(client_id ='LffVAg7jKO9CTA', client_secret = 'zJAotuk8q5p3Nfu9kJZBO7xWZYc', user_agent = 'Group6Project', username = 'Group6UoL', password = 'Group6')
reddit.read_only = True

def getNascarRace(series = 'mc', year='2019'):
	url = "http://api.sportradar.us/nascar-t3/{}/{}/races/schedule.json?api_key={}".format(series,year,nascar_key)
	result = requests.get(url)
	return result

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

def getNews(url="https://newsapi.org/v2/everything?",pageSize=20,apiKey="c78ac9726f714b79b3798843898a7400"):
	# Specify the query and number of returns
	parameters = {
    		'q': 'F1', # query phrase
    		'pageSize': 20,  # maximum is 100
    		'apiKey': apiKey # your own API key
	}

	# Make the request
	response = requests.get(url, params=parameters)

	# Convert to JSON
	#response_json = response.json()

	return response

def getReddit(sport):
	if sport == 'F1':
		subReddit = reddit.subreddit('formula1')
	elif sport == 'NASCAR':
		subReddit = reddit.subreddit('NASCAR')

	for sub in subReddit.hot(limit = 5):
		print(sub.title)
		print(sub.shortlink)
		print('')
	return


def menu():
	print("Please select which motorsport you would like:")
	msport = input("Choose from:\n> F1\n> NASCAR\n\n> ")
	msport.upper()

	motorsports = ['F1', 'NASCAR']
	date = datetime.today().strftime('%Y-%m-%d')

	while msport not in motorsports:
	    print("Please choose a valid option")
	    msport = input().upper()


	if msport == 'F1':
		f1_json = getF1Race().json()
		race = f1_json['MRData']['RaceTable']['Races'][0]
		circuit = race['Circuit']
		location = circuit['Location']

		print("Location: {}\nCircuit: {}".format(location['country'],circuit['circuitName']))
		weather = getWeather(location['locality']).json()
		news_json = getNews().json()
		headlines = []
		for i in news_json['articles']:
		    headlines.append(i['title'])

		pprint(weather)
		pprint(headlines)
		print('\nReddint posts: \n')
		getReddit(msport)

        
	elif msport == 'NASCAR':
		# Needs Completing
		nascar_json = getNascarRace().json()
		#pprint(nascar_json)


menu()
