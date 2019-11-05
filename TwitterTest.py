from twython import Twython
import json
import pandas as pd

with open("twitter_credentials.json", "r") as file:
    creds = json.load(file)
    
    
python_tweets = Twython(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])


query = {'q': '#F1',
        'result_type': 'popular',
        'count': 20,
        'lang': 'en',
    }
    
dict_ = {'user': [], 'date': [], 'text': [], 'favorite_count': []}
for status in python_tweets.search(**query)['statuses']:
    dict_['user'].append(status['user']['screen_name'])
    dict_['date'].append(status['created_at'])
    dict_['text'].append(status['text'])
    dict_['favorite_count'].append(status['favorite_count'])
    
df = pd.DataFrame(dict_)
df.sort_values(by='favorite_count', inplace=True, ascending=False)
df.head(5)