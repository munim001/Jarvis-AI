import sys
import speech_recognition as sr
import os
import pyttsx3
import webbrowser


def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def print_hi(name):
    print(f'Hi, {name}')

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold =  0.6
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Jarvis"


if __name__ == "__main__":
    say("Hello, I am Jarvis AI")
    print("Listening...")
    query = takeCommand()
    if "open youtube" in query:
        webbrowser.open("https://youtube.com")
    else:
        say(f"Sorry, I don't understand {query} Sir")

