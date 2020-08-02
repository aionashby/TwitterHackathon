#from __future__ import print_function
#import datetime
#import pickle
#import os.path
#import os
#import time
#import playsound
import speech_recognition as sr
# from gtts import gTTS
import pyttsx3
import pytz


def speak(text):
    # tts = gTTS(text=text, lang="en", slow=False)
    # filename = "voice.mp3"
    # tts.save(filename)
    # playsound.playsound(filename)
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(source)
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))
    return said.lower()

def get_timeline():
    speak("Here are the tweets on your timeline")

def make_tweet(text):
    speak("Tweet Posted!")

def hype():
    speak("Yay! I have followed the hype team members!")

def enact_robot():
    print("hi")
    WAKE = "hey twitter"
    speak("Start")
    program_execution = True

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(source)
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))
    return said.lower()

    while True:
        print("get audio")
        text = get_audio()
        print(text)

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
