import json
import ppy

def test():
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
  print("all done")

def content():
  aa = ppy("@BU_Tweets")
  if len(aa) == 0:
    print("error")
    return
  print("content is right")


if __name__ == '__main__':
  test()
  content();
