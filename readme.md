# api-design-szyszy315
## introduction
this project integrate twippy with google vision api to analysize images from a user's twitter. you can specify the user name and get the output in terminal.

Use twippy to extract tweets with images and store all the images in a json file. Then take the json file as input of google vision api to process all the images and show the results.
## User story
as a twitter user sometimes i want to analysize some user's twitter especially the one with images to get to know their habits.

## way to run this project
### 1.clone this repository<br>
```
git clone https://github.com/BUEC500C1/api-design-szyszy315.git
```
install requirments
```
pip3 install -r requirements.txt
```
### 2.set the twitter credential<br>
creat a file called twitter_credentials.py. The content should have 
```
CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""
```
### 3.set the google vision api credential 
Set the credentials according to https://cloud.google.com/docs/authentication/getting-started. Change the name of google credential as google.json in the same directory.
### 4.Then you can run imageapi.py<br>
```
python imageapi.py
```
the image url will be stored in a list in json file call twitter.json. The output of google vision will show in terminal.
Using twitter api to get image from twitter and describe the images via text using Google Vision.<br>
![image](https://github.com/BUEC500C1/api-design-szyszy315/blob/master/ec500.png)
