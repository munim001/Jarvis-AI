import pyttsx3
import speech_recognition as sr
import webbrowser

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def print_hi(name):
    print(f'Hi, {name}')

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio,language='en-in')
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some error occured: from Jarvis AI"


if __name__ == "__main__":
    say("Hello, I am Jarvis Sir")
    while True:
        print("Listening")
        query = takecommand()
        if "quit" in query.lower() or "exit" in query.lower():
            say("Goodbye Sir, shutting down Jarvis.")
            break
        sites = [["youtube","https://www.youtube.com"],
                 ["wikipedia","https://www.wikipedia.com"],
                 ["google","https://www.google.com"],
                 ["instagram","https://www.instagram.com"]]
        for site in sites:
            if f"open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} Sir...")
                webbrowser.open(site[1])

            elif "quit" in query.lower() or "exit" in query.lower():
                say("Goodbye Sir, shutting down Jarvis.")
                break



        # say(query)