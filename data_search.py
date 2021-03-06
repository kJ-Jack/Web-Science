import tweepy
import json
import csv
import pandas as pd
import os
import time

consumer_key= '05QRcauWKUjmG6NdoTaJ5RJlR'
consumer_secret= 'cl0cveUs3uKwoDk6jzqMP3NQDlyZqBqjF7LPVDybJehAcyZzjC'
access_token= '1225411734606884865-MQFToe2bFpBTo2WQMe1JM45h9ewqOq'
access_token_secret= 'xgO4gi1h4HY0g20JDGbnGjomZk1ztv11tI0fzzfRU5Ciq'

maxTweets = 150

path = './class'
emotion_class = {'excitement':['#excitement'],
                 'happy':['#happy'],
                 'pleasant':['#pleasant'], 
                 'surprise':['#surprise'],
                 'fear':['#fear'],
                 'angry':['#angry'],}

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)#, wait_on_rate_limit=True)#, proxy="127.0.0.1:1080")

print('Waiting...')

if (not api):
    print ("Can't Authenticate")
    sys.exit(-1)

if (not os.path.exists(path)):
    os.mkdir(path)

def create_class(emotion, text):
    pd_text = pd.DataFrame(text)
    print(pd_text)
    pd_text.to_csv(path +'/' + key +'.csv')

time_start=time.time()

for key in emotion_class.keys():
    every_time_start=time.time()
    number = 0
    text_list = []
    for tweet in tweepy.Cursor(api.search, q=emotion_class[key][0], lang='en', result_type="recent").items():
        find_other = False
        tw_inf = {}
        #check if the tweet contains other emotion
        for sub in emotion_class.keys():
            if ((emotion_class[sub][0] in tweet.text.lower()) and emotion_class[key][0]!=emotion_class[sub][0]):
                find_other = True
                break
        if (not find_other):
            number = number+1
            tw_inf['ID'] = number
            tw_inf['text'] = tweet.text
            tw_inf['created_at'] = tweet.created_at
            tw_inf['emotion'] = key
            text_list.append(tw_inf)
        if (number > maxTweets-1):
            break
    create_class(key, text_list)
    every_time_end=time.time()
    print('time cost: ',every_time_end-every_time_start,'s')
    print()

time_end=time.time()
print('Finished')
print('time cost: ',time_end-time_start,'s')
