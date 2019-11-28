import requests
import json
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
	'''
	Parameter: City 
	Type: String
	Description: Input a city name
	'''
	key = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=2e535070ac9219e3c58f19ac7227c197&'.format(city)
	try:
		result = json.loads(requests.get(key).content)
	except:
		# sth wrong with request
		return 'error'
	else:
		final_result = {
        # City name
		# MAX temp
		# MIN temp
		# Weather condiction
		# Weather description
		result['name'],
        str(result['main']['temp_max']),
        str(result['main']['temp_min']),
        result['weather'][0]['main'],
        result['weather'][0]['description']
    }
	return final_result


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


def getReddit(msport):
    base_url = 'https://www.reddit.com/'
    data = {'grant_type': 'password', 'username': 'Group6UoL', 'password': 'Group6'}
    auth = requests.auth.HTTPBasicAuth('IWrfJG6Tht2Ofw', 'mlrb5SiyS3TZjsvKUfW00L36d7Q')
    r = requests.post(base_url + 'api/v1/access_token',
                      data=data,
                      headers={'user-agent': 'University of Lincoln Group 6 by Group6UoL'},
                      auth=auth)
    d = r.json()
    
    token = 'bearer ' + d['access_token']
    base_url2 = 'https://oauth.reddit.com'
    headers = {'Authorization': token, 'User-Agent': 'University of Lincoln Group 6 by Group6UoL'}
    
    response = requests.get(base_url2 + '/api/v1/me', headers=headers)

    if response.status_code == 200:
        payload = {'g': 'Global', 'limit': 5}
        response = requests.get(base_url2 + '/r/formula1/new', headers=headers, params=payload)
        values = response.json()


                
        for i in range(len(values['data']['children'])):
            print(values['data']['children'][i]['data']['title'])
            print('https://www.reddit.com',values['data']['children'][i]['data']['permalink'])
            print('')


def menu():
	print("Please select which motorsport you would like:")
	msport = input("Choose from:\n> F1\n\n> ")
	msport.upper()

	motorsports = ['F1']
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
		weather = getWeather(location['locality'])
		news_json = getNews().json()
		headlines = []
		for i in news_json['articles']:
		    headlines.append(i['title'])

		pprint(weather)
		pprint(headlines)
		print('\nReddint posts: \n')
		getReddit(msport)

menu()
