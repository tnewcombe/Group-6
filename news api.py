import requests
import json

query = input("Please input a search query: ")

url = 'https://newsapi.org/v2/everything?q=' + query + '&from=' + '2019-10-25' + '&to=' + '2019-11-05' + '&sortBy=popularity&apiKey=c78ac9726f714b79b3798843898a7400'

# Make the request
response = requests.get(url)

# Convert to JSON
response_json = response.json()

titles = []
#for i in response_json['articles']:
#    titles.append(i['title'])
#    print(i['title'])
    
x = json.loads(response.text)

a = 1
for item in x['articles']:
    print(a, ' ', item['title'])
    titles.append(item['title'])
    print(' ')
    a+=1

desc = []
for i in x['articles']:
    desc.append(i['description'])
    
    


b = int(input())
print(titles[b-1])
print(desc[b-1])