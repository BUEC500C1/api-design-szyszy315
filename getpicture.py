#!/usr/bin/env python
# encoding: utf-8

import tweepy
import json
import twitter_credentials

def get_all_tweets(screen_name):
#Twitter API credentials
    auth = tweepy.OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
    auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
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

if __name__ == '__main__':
    #pass in the username of the account you want to download
    get_all_tweets(input('input the id'))
