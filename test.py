import json
import pyy

def testcontentofjson():
  tweets = []
  with open('tweet.json') as file:
    tweets = json.load(file)
  image_uri = tweets
  for i in tweets:
    if i.endswith("jpg"):
      continue
    else:
      print('error')
      return
  print("content of tweets is right")

def testtweetapi():
  aa = pyy.get_all_tweets("@BU_Tweets")
  if len(aa) == 0:
    print("error")
    return
  print("content is right")


if __name__ == '__main__':
  testcontentofjson()
  testtweetapi()
