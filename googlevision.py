import pyy
import json
from google.cloud import vision
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="ec500hw1-7326abd803ac.json"

def getdescription():
  tweets = []
  with open('tweet.json') as file:
    tweets = json.load(file)
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
  return len(response.label_annotations)

