# Sentiment Analytics with Python and Elastic Search
# https://realpython.com/blog/python/twitter-sentiment-python-docker-elasticsearch-kibana/

# Run the script directly from the command line with:
# python sentiment.py

# Ensure that the dependencies are installed in python
# via pip install: tweepy, textblob, elasticsearch



import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from textblob import TextBlob
from elasticsearch import Elasticsearch
from datetime import datetime

# import twitter keys and tokens
from config import *

# create instance of elasticsearch
es = Elasticsearch()

indexName = "test_new_fields"

class TweetStreamListener(StreamListener):

    # on success
    def on_data(self, data):

        # decode json
        dict_data = json.loads(data) # data is a json string
        
        # print(data) # to print the twitter json string
        print(dict_data)

        # pass tweet into TextBlob
        tweet = TextBlob(dict_data["text"])

        # print (tweet.sentiment.polarity) # output sentiment polarity

        # determine if sentiment is positive, negative, or neutral
        if tweet.sentiment.polarity < 0:
            sentiment = "negative"
        elif tweet.sentiment.polarity == 0:
            sentiment = "neutral"
        else:
            sentiment = "positive"

        # output polarity sentiment and tweet text
        print (str(tweet.sentiment.polarity) + " " + sentiment + " " + dict_data["text"])

        # add text and sentiment info to elasticsearch
        es.index(index=indexName,
                 doc_type="test-type",
                 body={"author": dict_data["user"]["screen_name"],
                       "date": dict_data["created_at"], # unfortunately this gets stored as a string
                       "location": dict_data["user"]["location"], # user location
                       "followers": dict_data["user"]["followers_count"],
                       "friends": dict_data["user"]["friends_count"],
                       "time_zone": dict_data["user"]["time_zone"],
                       "lang": dict_data["user"]["lang"],
                       #"timestamp": float(dict_data["timestamp_ms"]), # double not recognised as date 
                       "timestamp": dict_data["timestamp_ms"],
                       "datetime": datetime.now(),
                       "message": dict_data["text"],
                       "polarity": tweet.sentiment.polarity,
                       "subjectivity": tweet.sentiment.subjectivity,
                       # handle geo data
                       #"coordinates": dict_data[coordinates],
                       "sentiment": sentiment})
        return True

    # on failure
    def on_error(self, status):
        print (status)

if __name__ == '__main__':

    # create instance of the tweepy tweet stream listener
    listener = TweetStreamListener()

    # set twitter keys/tokens
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # create instance of the tweepy stream
    stream = Stream(auth, listener)

    # search twitter for these keywords
    stream.filter(track=['#EUref', '#Brexit'])