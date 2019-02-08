import tweepy
import simplejson as json
from tweepy import OAuthHandler
from textblob import TextBlob
from tweepy import Stream
from tweepy.streaming import StreamListener

consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

# Download my timeline
def timeline():
    for status in tweepy.Cursor(api.home_timeline).items(20):
        print(status.text)
        print()
        print('-------')
        print()

#Stream
class MyListener(StreamListener):

    def __init__(self,api=None):
        super(StreamListener,self).__init__()
        self.num_tweets = 0
        self.subjectivity = 0
        self.polarity = 0

    def on_data(self,data):

        try:
            with open('Brexit.json','a') as f:
                if 'lang' in data:
                    if json.loads(data)['lang'] == 'en':
                        text = TextBlob(json.loads(data)['text'])
                        sentiment = text.sentiment
                        self.polarity += text.sentiment.polarity
                        self.subjectivity += text.sentiment.subjectivity
                        f.write(data)
                        self.num_tweets +=1
                        if self.num_tweets < 20:
                            return True
                        else:
                            return False
        except BaseException as e:
                print('Error on_data: %s' % str(e))
        return True
        
    def on_error(self, status):
        print('Error: ', status)
        return False

twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['BTT'])


twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['hilary'])

print('------Fin--------------')
testimonial = TextBlob("I'm bored")
print(testimonial.sentiment)