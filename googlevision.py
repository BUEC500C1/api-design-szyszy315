import getpicture
import json
from google.cloud import vision

def getdescription(tweets):
  image_uri = tweets
  for i in image_uri:
    client = vision.ImageAnnotatorClient()
    image = vision.types.Image()
    image.source.image_uri = i

    response = client.label_detection(image=image)

    print('Labels (and confidence score):')
    print('=' * 79)
    for label in response.label_annotations:
      print(f'{label.description} ({label.score*100.:.2f}%)')


if __name__ == '__main__':
  getpicture.get_all_tweets(input('input id'))
#get tweets
  tweets = []
  with open('tweet.json') as file:
    tweets = json.load(file)
  getdescription(tweets)
