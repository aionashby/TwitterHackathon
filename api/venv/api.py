import time
import speechtotxt
from flask import Flask

app = Flask(__name__)

@app.route('/time')
def get_current_time():  
    return {'time': time.time()}

@app.route('/make_tweet/<tweet>')
def tweet_string(tweet):
  return {'text': "The tweet is " + str(tweet)}

