import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclib
import requests
from gtts import gTTS


recognizer=sr.Recognizer()
engine=pyttsx3.init()
newsapi="09f453b9cad240e1a89407963dcce6da"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link=musiclib.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r=requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=09f453b9cad240e1a89407963dcce6da")
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])

            for article in articles:
                speak(article['title'])
   
  

if __name__=="__main__":
    speak("Initializing Jarvis...!")
    while True:
        r = sr.Recognizer()
        

        print("recognising....!")
        try:
            with sr.Microphone() as source:
                print("Listening....!")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower()=="jarvis"):
                speak("yes sir!...")
                with sr.Microphone() as source:
                    print("Jarvis Active....!")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))