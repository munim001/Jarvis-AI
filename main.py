import sys
import speech_recognition as sr
import os
import pyttsx3


def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def print_hi(name):
    print(f'Hi, {name}')

# def takeCommand():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:


if __name__ == "__main__":
    say("Hello, I am Jarvis AI")
