# from __future__ import print_function
# import datetime
# import pickle
# import os.path
# from googleapiclient.discovery import build
# from google_auth_oauthlib.flow import InstalledAppFlow
# from google.auth.transport.requests import Request
# import os
# import time
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
            print("Exception: " + str(e))
    return said.lower()

def get_timeline():
    # do timeline processing here
    speak("Here are the tweets on your timeline")

def make_tweet(text):
    # do making a tweet processing here
    speak("Tweet Posted!")

def hype():
    # do hype team processing here
    speak("Yay! I have followed the hype team members!")

WAKE = "hey twitter"
print("Start")
program_execution = True

while program_execution:
    text = get_audio()

    if text.count(WAKE) > 0:
        speak("Hi Aarushi. What would you like to do?")
        text = get_audio()

    TIMELINE_KEYWORDS = ["what is on my newsfeed", "what is on my timeline", "show me some tweets", "show me my newsfeed", "show me my timeline"]
    for phrase in TIMELINE_KEYWORDS:
        if phrase in text:
            get_timeline()

    TRENDING_KEYWORDS = ["what is trending", "what is popular", "what is happening"]

    TWEET_KEYWORDS = ["make a tweet", "make a new tweet", "tweet something"]
    for phrase in TWEET_KEYWORDS:
        if phrase in text:
            speak("What would you like me to tweet?")
            tweet_text = get_audio()
            make_tweet(tweet_text)

    HYPE_KEYWORDS = ["hype me up"]
    for phrase in HYPE_KEYWORDS:
        if phrase in text:
            hype()

    GOODBYE_KEYWORDS = ["goodbye", "bye"]
    for phrase in GOODBYE_KEYWORDS:
        if phrase in text:
            program_execution = False
# - follow person
# - read tweets on timeline
# - read tweets with certain words
