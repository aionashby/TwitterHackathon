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
        self.api = tweepy.API(self.auth, wait_on_rate_limit=True)

    def get_home_time_line(self):
        home_time_line = self.api.home_timeline()
        counter = 10

        if len(self.tweets) != 0:
            self.tweets = deque([])

        for tweet in home_time_line:
            if counter > 0:
                self.tweets.append(tweet)
                counter -= 1

    def like_current_tweet_in_queue(self):

        try:
            front_of_queue = self.tweets[0]
            front_of_queue.favorite()
        except tweepy.TweepError as e:
            print(e.reason)

    def retweet_current_tweet_in_queue(self):
        try:
            front_of_queue = self.tweets[0]
            front_of_queue.retweet()
        except tweepy.TweepError as e:
            print(e.reason)

    def dequeue_tweet_queue(self):
        try:
            last_tweet = self.tweets.popleft()
            return last_tweet
        except tweepy.TweepError as e:
            print(e.reason)

    def peek_at_current_tweet(self):
        if len(self.tweets) != 0:
            return self.tweets[0]
        else:
            return

    def create_new_tweet(self, tweet):  # posts new tweet, tweet variable is a string
        if self.api != None:
            self.api.update_status(tweet)
        else:
            return

    def print_tweets(self):
        for tweet in self.tweets:
            print(tweet.text)

    def HYPE_ME_UP(self):

        hype_team = ["itsjulieromero", "Hummmmmbaby",
                     "rheanamariee", "StoicLeys"]

        for user in hype_team:
            try:
                self.api.create_friendship(user)
            except tweepy.TweepError as e:
                print(e.reason)

    def TONE_IT_DOWN(self):
        hype_team = ["itsjulieromero", "Hummmmmbaby",
                     "rheanamariee", "StoicLeys"]

        for user in hype_team:
            try:

                self.api.destroy_friendship(user)

            except tweepy.TweepError as e:
                print(e.reason)


t = Tweety(user.CONSUMER_KEY, user.CONSUMER_SECRET,
           user.ACCESS_TOKEN, user.ACCESS_TOKEN_SECRET)

t.authenticate_api()

t.get_home_time_line()

t.print_tweets()

# t.HYPE_ME_UP()
# t.TONE_IT_DOWN()
