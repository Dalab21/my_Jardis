import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import pywhatkit
import os


engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#speak("Hello world")

def commands():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        r.adjust_for_ambient_noise(source, duration=1) # ligne de code à commenter en cas d'erreur
        audio = r.listen(source)
    try:
        print("Wait for Few Moments...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You just said: {query}\n")
    except Exception as e:
        print(e)
        speak("Please Tell me again")
        query="none"
    return query

#query=commands().lower()

def wishings():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour < 12 :
        print("Good Morning, Sir")
        speak("Good Morning, Sir")
    
    elif hour >=12 and hour < 17 :
        print("Good Afternoon, Sir")
        speak("Good Afternoon, Sir")
    
    elif hour >=17 and hour < 21 :
        print("Good Evening, Sir")
        speak("Good Evening, Sir")

    else:
        print("Good Night, Sir")
        speak("Good Night, Sir")


if __name__ == "__main__":
    wishings()
    query=commands().lower()
    if 'time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        print(strTime)
        speak(f"Sir, the time is {strTime}")

    elif 'open firefox' in query:
        speak("Opening Firepox Application Sir ...")
        os.startfile('C:/Program Files/Mozilla Firefox/firefox.exe')

    elif 'wikipedia' in query:
        speak("searching in Wikipedia...")
        try:
            query=query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("According to Wikipedia, ")
            print(results)
            speak(results)
        except:
            speak("No results found...")
            print("No results found...")
        
    elif 'youtube' in query:
        speak("Searching in youtube...")
        try:
            query=query.replace("search on youtube", "").replace("youtube", "")
            pywhatkit.playonyt()
        except:
            speak("No results found")
            print("No results found...")

