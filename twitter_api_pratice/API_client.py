from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import user
# 420 error means your accessing too many tweets .


class TwitterStreamer():
    """
    Class for streaming and processing live tweets.

    """

    def __init__(self):
        pass

    def stream_tweets(self, fetched_tweets_filename, hash_tag_list):
        # this handle twitter auth. and the connection to the twitter api
        # create an instance of the class we created
        listener = StdOutListener(fetched_tweets_filename)

        # authenticates te user
        auth = OAuthHandler(user.CONSUMER_KEY, user.CONSUMER_SECRET)

        # authenitcates the user's tokens
        auth.set_access_token(user.ACCESS_TOKEN, user.ACCESS_TOKEN_SECRET)

        # we create a usuable instance of the stream class
        stream = Stream(auth, listener)

        # we need to filter tweets
        # track helps us filter the tweets by the objects

        stream.filter(track=hash_tag_list)


class StdOutListener(StreamListener):
    """
    This is a basic listern class that just prints recieved tweets to stdout
    """

    def __init__(self, fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename

    def on_data(self, data):
        try:
            print(data)
            with open(self.fetched_tweets_filename, "a") as tf:
                tf.write(data)
            return True
        except BaseException as e:
            print("Error on_data: %s" + str(e))
        return True

    def on_error(self, status):
        print(status)


if __name__ == "__main__":
    hash_tag_list = ['donald trump',  'bernie sanders']
    fetched_tweets_filename = "tweets.json"
    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(fetched_tweets_filename, hash_tag_list)
