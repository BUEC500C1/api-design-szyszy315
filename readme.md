# api-design-szyszy315


## 1.clone this repository<br>
```
git clone https://github.com/BUEC500C1/api-design-szyszy315.git<br>
```
## 2.set the twitter credential<br>
creat a file called twitter_credentials.py. The content should have 
```
CONSUMER_KEY = "zyXZcDkT4POyuxv69L7sc86DQ"
CONSUMER_SECRET = "hA6ke1yMjPLUlyZgpDX7Uizp25IMfWaqAmA5A84d1edYs7vEGi"
ACCESS_TOKEN = "1167378411137961984-CKJmb3bCzvN215Y1CW1GaxaHLTEKAg"
ACCESS_TOKEN_SECRET = "2iQFkD0sprvlhIYunooaSTIK6mHdI9nrnIFM4LqOyACWW"
```
## 3.set the google vision api credential 
Set the credentials according to https://cloud.google.com/docs/authentication/getting-started.
## 4.Then you can run imageapi.py<br>
```
python imageapi.py
```
the image url will be stored in a list in json file call twitter.json. The output of google vision will show in terminal.
Using twitter api to get image from twitter and describe the images via text using Google Vision.<br>
![image](https://github.com/BUEC500C1/api-design-szyszy315/blob/master/ec500.png)
