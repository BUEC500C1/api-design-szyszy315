import json
import pyy
import googlevision
import pytest

def test_contentofjson():
  tweets = []
  with open('tweet.json') as file:
    tweets = json.load(file)
  image_uri = tweets
  for i in tweets:
    if i.endswith("jpg"):
      continue
    else:
      print('error:jsonfile')
      return
  print("content of tweets is right")

def test_tweetapi():
  aa = pyy.get_all_tweets("@BU_Tweets")
  if len(aa) == 0:
    print("error:twitterapi")
    return
  print("twitter api works")

def test_googlevision():
  l = googlevision.getdescription()
  if (l == 0):
    print("error: googlevision")
  else:
    print("googlevision works")


