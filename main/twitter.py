from django.conf import settings
settings.configure(settings)
import tweepy
import csv
from tweepy import OAuthHandler
import json
#from models import people, events
tweet_list = []
WORDS = ['popular_kids', 'ATXHackathon']

consumer_key = 'oOJIn75tTIrfhqQWyasOi76NN'
consumer_secret = '76G1rS4SPl2iDy9oNHKzLWvvlCpwOrKfrgW3tKVjzkJbGs5NWl'
access_token = '26798542-jYR8XfDZiwWEZQSjwdRcMeIa7HJX87X9pZIIKUEE4'
access_secret = 'vU0CP4x7i6HlMModmHLOb6UhSHP1EiFGXnmm7vsN8DWIY'
class StreamListener(tweepy.StreamListener):
    #This is a class provided by tweepy to access the Twitter Streaming API.

    def on_connect(self):
        # Called initially to connect to the Streaming API
        print("You are now connected to the streaming API.")

    def on_error(self, status_code):
        # On error - if an error occurs, display the error / status code
        print('An Error has occured: ' + repr(status_code))
        return False

    def on_data(self, data):
        #This is the meat of the script...it connects to your mongoDB and stores the tweet
        try:
            # Decode the JSON from Twitter
            datajson = json.loads(data)
            #
            tweet_list.append(datajson)
            #grab the 'created_at' data from the Tweet to use for display
            created_at = datajson['created_at']

            #print out a message to the screen that we have collected a tweet
            print("Tweet collected at " + str(created_at))

            #insert the data into the mongoDB into a collection called twitter_search
            #if twitter_search doesn't exist, it will be created.
            #db.twitter_search.insert(datajson)
            f = open('db.csv', 'wb')
            w = csv.writer(f,delimiter='|')
            uname = datajson['user']['screen_name']
            tw_type = 'tw_ment'
            text = datajson['text']
            post_id = datajson['id']
            print ("uname:", uname)
            print ("text:", text)
            event_list = [uname,tw_type,created_at,text,post_id]
            w.writerow(event_list)

            f.close()

            #event = events(person_id=datajson['screen_name'],event_type='tw_ment',score_increment=event_dictionary['tw_ment'],text=datajson['text'],node_id=datajson['id'])
            #event.save()
        except Exception as e:
           print(e)

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

listener = StreamListener(api=tweepy.API(wait_on_rate_limit=True))
streamer = tweepy.Stream(auth=auth, listener=listener)
print("Tracking: " + str(WORDS))
streamer.filter(track=WORDS, async=True)
