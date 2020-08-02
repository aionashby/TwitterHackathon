# from __future__ import print_function
# import datetime
# import pickle
# import os.path
# from googleapiclient.discovery import build
# from google_auth_oauthlib.flow import InstalledAppFlow
# from google.auth.transport.requests import Request
# import os
# import time
import user
from tweety_class import Tweety
import speech_recognition as sr
import pyttsx3
import pytz

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("I couldn't hear you. Try again")
    return said.lower()

def like_tweet(t):
    t.like_current_tweet_in_queue()
    speak("I have liked the tweet")

def retweet_tweet(t):
    t.retweet_current_tweet_in_queue()
    speak("I have retweeted the tweet")

def get_timeline(t):
    # do timeline processing here
    t.get_home_time_line()
    speak("Here are the tweets on your timeline")
    continue_tweets = True
    while continue_tweets:
        print(t.peek_at_current_tweet().text)
        speak(t.peek_at_current_tweet().text)
        speak("Do you want to like or retweet this tweet? Say cancel to stop.")
        text = get_audio()
        if "like" in text:
            like_tweet(t)
        if "retweet" in text:
            retweet_tweet(t)
        if "cancel" in text:
            break
        speak("Onto the next tweet")
        t.dequeue_tweet_queue()
        

def make_tweet(t, text):
    if(t.create_new_tweet(text)):
        speak("Tweet Posted!")
    else:
        speak("Unable to Post Tweet at this time.")
    # do making a tweet processing here
    

def hype(t):
    # do hype team processing here
    t.HYPE_ME_UP()
    speak("Yay! I have followed the hype team members! Rheana, Julie, and Kelly <3")

def tone_down(t):
    # do hype team processing here
    t.TONE_IT_DOWN()
    speak("Sad! I have unfollowed the hype team members!")

def search_tweet(t, search):
    # do hype team processing here
    t.search_tweets(search)
    speak("Here are the search results for " + search)
    continue_tweets = True
    while continue_tweets:
        print(t.peek_at_current_tweet().text)
        speak(t.peek_at_current_tweet().text)
        speak("Do you want to like or retweet this tweet? Say cancel to stop.")
        text = get_audio()
        if "like" in text:
            like_tweet(t)
        if "retweet" in text:
            retweet_tweet(t)
        if "cancel" in text:
            break
        speak("Onto the next tweet")
        t.dequeue_tweet_queue()

def trending_tweets(t):
    # do hype team processing here
    t.get_trends()
    speak("Here are the top trending topics")
    continue_tweets = 0
    while continue_tweets < 10:
        print(t.peek_at_current_trend())
        speak(t.peek_at_current_trend())
        t.dequeue_trend_queue()
        continue_tweets = continue_tweets + 1

# EXECUTION CODE
WAKE = "hey twitter"

# set up API
t = Tweety(user.CONSUMER_KEY, user.CONSUMER_SECRET,
           user.ACCESS_TOKEN, user.ACCESS_TOKEN_SECRET)
t.authenticate_api()

# alert user we are ready
print("I am awake!")
program_execution = True

while program_execution:
    text = get_audio()

    if text.count(WAKE) > 0:
        speak("Hi Aarushi. Ask me a question!")
        text = get_audio()

    TIMELINE_KEYWORDS = ["what is on my newsfeed", "what is on my timeline", "show me some tweets", "show me my newsfeed", "show me my timeline"]
    for phrase in TIMELINE_KEYWORDS:
        if phrase in text:
            get_timeline(t)

    TWEET_KEYWORDS = ["make a tweet", "make a new tweet", "tweet something"]
    for phrase in TWEET_KEYWORDS:
        if phrase in text:
            speak("What would you like me to tweet?")
            tweet_text = get_audio()
            make_tweet(t, tweet_text)

    SEARCH_KEYWORDS = ["search for tweets", "search" "find tweets"]
    for phrase in SEARCH_KEYWORDS:
        if phrase in text:
            speak("What would you like me to search for?")
            tweet_text = get_audio()
            search_tweet(t, tweet_text)

    TRENDING_KEYWORDS = ["what is trending", "what is popular", "what is happening"]
    for phrase in TRENDING_KEYWORDS:
        if phrase in text:
            trending_tweets(t)

    HYPE_KEYWORDS = ["hype me up"]
    for phrase in HYPE_KEYWORDS:
        if phrase in text:
            hype(t)

    TONE_KEYWORDS = ["tone it down"]
    for phrase in TONE_KEYWORDS:
        if phrase in text:
            tone_down(t)

    GOODBYE_KEYWORDS = ["goodbye", "bye"]
    for phrase in GOODBYE_KEYWORDS:
        if phrase in text:
            program_execution = False
speak("Goodbye Aarushi")
# - follow person
# - read tweets on timeline
# - read tweets with certain words
