import googlevision
import pyy

def vision():
  name = input("input name")
  pyy.get_all_tweets(name)
  googlevision.getdescription()
  
if __name__ == '__main__':
  vision()
