import tweepy
import simplejson as json
from tweepy import OAuthHandler
from textblob import TextBlob
from tweepy import Stream
from tweepy.streaming import StreamListener

#Stream
class MyListener(StreamListener):

    def __init__(self,api=None):
        super(StreamListener,self).__init__()
        self.num_tweets = 0
        self.subjectivity = 0
        self.polarity = 0
        self.maxTweets = 5

    # Everytime recibes a tweet:
    # if 'lang' in data:
    #    if json.loads(data)['lang'] == 'en':

    def on_data(self,data):
        try:
            with open('Output.json','a') as f:
                if 'lang' in data:
                    if json.loads(data)['lang'] == 'en':

                        text = TextBlob(json.loads(data)['text'])
                        sentiment = text.sentiment
                        self.polarity += text.sentiment.polarity
                        self.subjectivity += text.sentiment.subjectivity

                        f.write(data)
                        self.num_tweets += 1

                        if self.num_tweets < self.maxTweets:
                            return True
                        else:
                            print('Polarity: %s' % str(self.polarity / self.maxTweets))
                            print('Subjectivity: %s' % str(self.subjectivity / self.maxTweets))
                            return False
        except BaseException as e:
                print('Error on_data: %s' % str(e))
        return True
        
    def on_error(self, status):
        print('Error: ', status)
        return False