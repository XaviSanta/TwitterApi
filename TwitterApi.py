import tweepy
import simplejson as json
from tweepy import OAuthHandler
from textblob import TextBlob
from tweepy import Stream
from tweepy.streaming import StreamListener
from MyListener import MyListener

class TwitterApi:
    # consumer_key = ''
    # consumer_secret = ''
    # access_token = ''
    # access_secret = ''

    api = ''
    auth = ''

    def __init__(self):
        self.auth = OAuthHandler(self.consumer_key, self.consumer_secret)
        self.auth.set_access_token(self.access_token, self.access_secret)
        self.api = tweepy.API(self.auth)

    # Download my timeline
    def timeline(self):
        for status in tweepy.Cursor(self.api.home_timeline).items(20):
            print(status.text)
            print('-------')

    # Stream of tweets that contain 'word'
    def tweetStream(self, word):
        twitter_stream = Stream(self.auth, MyListener())
        twitter_stream.filter(track=[word])