#!/usr/bin/env python
# encoding: utf-8

import tweepy
import json
import keys

def get_all_tweets(screen_name):
#Twitter API credentials
    auth = tweepy.OAuthHandler(keys.CONSUMER_KEY, keys.CONSUMER_SECRET)
    auth.set_access_token(keys.ACCESS_TOKEN, keys.ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    alltweets = {}


    for status in tweepy.Cursor(api.user_timeline,id=screen_name,count = 50).items(50):
        if 'media' in status.entities:
            for image in status.entities['media']:
                print(image['media_url'])
                alltweets[image['media_url']] = status.favorite_count + status.retweet_count

                print ("...{} tweets downloaded so far".format(len(alltweets)))
    tweets_ranking=sorted(alltweets ,key = lambda x : alltweets[x])

    #write tweet objects to JSON
    file = open('tweet.json', 'w')
    print ("Writing tweet objects to JSON please wait...")
    json.dump(tweets_ranking,file,indent = 4)
    print ("Done")
    file.close()
    return tweets_ranking