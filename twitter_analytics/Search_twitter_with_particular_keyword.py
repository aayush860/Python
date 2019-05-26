from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
from twitter import *
import json

ACCESS_TOKEN = "xxxx"
ACCESS_SECRET = "xxxxx"
CONSUMER_KEY = "Jxxxxx"
CONSUMER_SECRET = "xxxxxxq4Wl"

uth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
#print uth

twitter=Twitter(auth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET))

twitter_stream = TwitterStream(auth=uth)
#print twitter_stream



query = twitter.search.tweets(q = "dog")
print "Search complete (%.3f seconds)" % (query["search_metadata"]["completed_in"])
print len(query)
x=0

for t in query["search_metadata"]:
    print t
for res in query["statuses"]:
    print res["user"]["screen_name"]
    print "end of line"
    x=x+1
print x


xxx=twitter_stream.statuses.filter(track = "")        #if smone is posting live

tt=0

#for rr in xxx:
#    print rr

for pin in xxx:
    tt=tt+1
    print tt
    if tt<50:
        print pin["user"]["screen_name"]
        print pin["text"]
    else:
        break
