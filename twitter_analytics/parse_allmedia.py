from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
from twitter import *
import json


ACCESS_TOKEN = "xxxx"
ACCESS_SECRET = "xxxxx"
CONSUMER_KEY = "Jxxxxx"
CONSUMER_SECRET = "xxxxxxq4Wl"

uth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

twitter=Twitter(auth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET))

twitter_stream = TwitterStream(auth=uth)

username=""                         ##INPUT THE TWITTER USERNAME

results = twitter.statuses.user_timeline(screen_name = username,count=300)                #user retwetted
#print results.entities.get['media',[{}]]
cou=0
for d in results:
    try:
        dd=d["extended_entities"]["media"]
        for ddd in dd:
            
            for ww in ddd["video_info"]["variants"]:
                print ww["url"]
                print "eol"
                cou=cou+1
                
    except:
        pass


#print i["description"]["video_info"]
print "\n\n"
for t in results:
    try:
        ee=t["entities"]["media"]
        for eee in ee:
            print eee["media_url"]
            print "\n"
            cou=cou+1
    except:
        pass
print cou
#for media in results.entities.get("media",[{}]):
#    print media

