import requests
from pprint import pprint

city = input("City name: ")
key = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=2e535070ac9219e3c58f19ac7227c197&q='.format(city)

res = requests.get(key)
data = res.json()

pprint(res)
pprint(data)