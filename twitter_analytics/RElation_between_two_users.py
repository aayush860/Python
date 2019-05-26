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

source=""
target=""

result = twitter.friendships.show(source_screen_name = source,target_screen_name = target)

#print result
following = result["relationship"]["target"]["following"]
follows   = result["relationship"]["target"]["followed_by"]

print "%s following %s: %s" % (source, target, follows)
