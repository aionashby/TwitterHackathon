import tweepy
import user
from collections import deque


class Tweety():
    def __init__(self, CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET):
        self.auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        self.auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        self.tweets = deque([])
        self.trends = deque([])
        self.api = None

    # implemented
    def authenticate_api(self):
        try:
            self.api = tweepy.API(self.auth, wait_on_rate_limit=True)
        except tweepy.TweepError as e:
            print(e.reason)

    def get_trends(self):
        usaTrends = self.api.trends_place(23424977)
        trendData = usaTrends[0]

        trends = trendData['trends']
        self.trends = deque([trend['name'] for trend in trends[:10]])

    def dequeue_trend_queue(self):
        try:
            last_trend = self.trends.popleft()
            return last_trend
        except tweepy.TweepError as e:
            print(e.reason)

    def peek_at_current_trend(self):
        if len(self.trends) != 0:
            return self.trends[0]
        else:
            return

    # implemented
    def get_home_time_line(self):
        self.tweets = deque([])
        home_time_line = self.api.home_timeline()
        counter = 10

        if len(self.tweets) != 0:
            self.tweets = deque([])

        for tweet in home_time_line:
            if counter > 0:
                self.tweets.append(tweet)
                counter -= 1

    # implemented
    def like_current_tweet_in_queue(self):
        try:
            front_of_queue = self.peek_at_current_tweet()
            front_of_queue.favorite()
        except tweepy.TweepError as e:
            print(e.reason)

    # implemented
    def retweet_current_tweet_in_queue(self):
        try:
            front_of_queue = self.peek_at_current_tweet()
            front_of_queue.retweet()
        except tweepy.TweepError as e:
            print(e.reason)

    # implemented
    def dequeue_tweet_queue(self):
        try:
            last_tweet = self.tweets.popleft()
            return last_tweet
        except tweepy.TweepError as e:
            print(e.reason)

    # implemented
    def peek_at_current_tweet(self):
        if len(self.tweets) != 0:
            return self.tweets[0]
        else:
            return

    # implemented
    def create_new_tweet(self, tweet):  # posts new tweet, tweet variable is a string
        if self.api != None:
            self.api.update_status(tweet)
        else:
            return

    # implemented
    def print_tweets(self):
        for tweet in self.tweets:
            print(tweet.text)

    # implemented
    def search_tweets(self, title):
        self.tweets = deque([])
        try:

            temp_tweets = self.api.search(title)
            counter = 10

            for tweet in temp_tweets:
                self.tweets.append(tweet)
                if counter < 1:
                    break
                counter -= 1

        except tweepy.TweepError as e:
            print(e.reason)

    # implemented
    def HYPE_ME_UP(self):

        hype_team = ["itsjulieromero", "Hummmmmbaby",
                     "rheanamariee"]

        for user in hype_team:
            try:
                self.api.create_friendship(user)
            except tweepy.TweepError as e:
                print(e.reason)

    # implemented
    def TONE_IT_DOWN(self):
        hype_team = ["itsjulieromero", "Hummmmmbaby",
                     "rheanamariee"]

        for user in hype_team:
            try:

                self.api.destroy_friendship(user)

            except tweepy.TweepError as e:
                print(e.reason)