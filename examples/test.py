from TwitterApi import TwitterApi

api = TwitterApi()

# api.timeline()
api.tweetStream("Trump")
print('------End--------------')