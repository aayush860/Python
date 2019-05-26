from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
from twitter import *
import json

ACCESS_TOKEN = "xxxx"
ACCESS_SECRET = "xxxxx"
CONSUMER_KEY = "Jxxxxx"
CONSUMER_SECRET = "xxxxxxq4Wl"

uth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
print uth

twitter=Twitter(auth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET))

twitter_stream = TwitterStream(auth=uth)
print twitter_stream

username=""

query = twitter.friends.ids(screen_name = username)                         #all userids of following
print query[u'ids']


results = twitter.statuses.user_timeline(screen_name = username)                #user retwetted
print len(results)
#print results[media_url_https"]
for t in results:
    try:
        print (t["extended_entities"])
    except:
        pass
#subquery = twitter.users.lookup(screen_name = username)
#print subquery
#for t in query[3]:
    #subquery = twitter.users.lookup(user_id = t)
    #print subquery
#    print t


#us=twitter.GetUserTimeline(screen_name=username)
#print us
#sn=twitter.screen_name(username)
#print sn

