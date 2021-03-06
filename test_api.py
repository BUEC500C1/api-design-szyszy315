import json
import pyy
import googlevision
import pytest

#test if the content of json file in right format
def testcontentofjson():
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

  #test if get images from twitter
def testtweetapi():
  aa = pyy.get_all_tweets("@BU_Tweets")
  if len(aa) == 0:
    print("error:twitterapi")
    return
  print("twitter api works")

  #test output of google vision
def testgooglevision():
  l = googlevision.getdescription()
  if (l == 0):
    print("error: googlevision")
  else:
    print("googlevision works")

def test_api():
  testcontentofjson()
  testtweetapi()
  testgooglevision()
