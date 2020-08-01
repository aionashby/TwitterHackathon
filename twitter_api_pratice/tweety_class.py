import tweepy
import user
from collections import deque

# # authenticates te user
# auth = tweepy.OAuthHandler(user.CONSUMER_KEY, user.CONSUMER_SECRET)

# # authenitcates the user's tokens
# auth.set_access_token(user.ACCESS_TOKEN, user.ACCESS_TOKEN_SECRET)


# api = tweepy.API(auth)


# tweets_on_timeline = api.home_timeline()

# for tweet in tweets_on_timeline:
#     print(tweet)


class Tweety():
    def __init__(self, CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET):
        self.auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        self.auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        self.tweets = deque([])
        self.trends = deque([])
        self.api = None

    def authenticate_api(self):
        self.api = tweepy.API(self.auth)

    def get_home_time_line(self):
        home_time_line = self.api.home_timeline()
        counter = 10

        if len(self.tweets) != 0:
            self.tweets = deque([])

        for tweet in home_time_line:
            if counter > 0:
                self.tweets.append(tweet)
                counter -= 1


t = Tweety(user.CONSUMER_KEY, user.CONSUMER_SECRET,
           user.ACCESS_TOKEN, user.ACCESS_TOKEN_SECRET)

t.authenticate_api()

t.get_home_time_line()

for tweet in t.tweets:
    print(tweet)
