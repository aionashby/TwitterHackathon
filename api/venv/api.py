import time
import speechtotxt
from flask import Flask
import user
from tweety_class import Tweety

app = Flask(__name__)

t = Tweety(user.CONSUMER_KEY, user.CONSUMER_SECRET,
           user.ACCESS_TOKEN, user.ACCESS_TOKEN_SECRET)
t.authenticate_api()

@app.route('/time')
def get_current_time():  
    return {'time': time.time()}

@app.route('/hype')
def follow_hype_team():  
    t.HYPE_ME_UP()
    return {'response': "Sucesss! I have followed all the hype team members: Kelly, Rheana, and Julie <3"}

@app.route('/tone')
def unfollow_hype_team():  
    t.TONE_IT_DOWN()
    return {'response': "Sad... I have unfollowed all the hype team members: Kelly, Rheana, and Julie </3"}

@app.route('/create/<tweet>')
def tweet_string(tweet):
    t.create_new_tweet(tweet)
    return {'response': "I have posted that tweet!"}

@app.route('/trends')
def get_trends():
    t.get_trends()
    trends = "The Top 10 Trending Topics Are: "
    count = 0 
    while count < 10:
        trends += str(t.peek_at_current_trend())
        trends += ", "
        t.dequeue_trend_queue()
        count = count + 1
    return {'response': trends}

