#!/usr/bin/env python
# coding: utf-8

# In[13]:


import praw

reddit = praw.Reddit(client_id ='LffVAg7jKO9CTA',
                    client_secret = 'zJAotuk8q5p3Nfu9kJZBO7xWZYc',
                    user_agent = 'Group6Project',
                    username = 'Group6UoL',
                    password = 'Group6')

reddit.read_only = True

F1 = reddit.subreddit('formula1')

for sub in F1.new(limit = 10):
    print(sub.title)
    print(sub.shortlink)
    print('\n')

