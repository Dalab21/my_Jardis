import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import pywhatkit
import os

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # voix "French"

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def commands():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Écoute...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        print("Patientez quelques instants...")
        query = r.recognize_google(audio, language='fr-FR')
        print(f"Vous venez de dire : {query}\n")
    except Exception as e:
        print(e)
        speak("Veuillez répéter")
        query = "none"
    return query

def wishings():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        print("Bonjour, Monsieur")
        speak("Bonjour, Monsieur")

    elif hour >= 12 and hour < 17:
        print("Bonne après-midi, Monsieur")
        speak("Bonne après-midi, Monsieur")

    elif hour >= 17 and hour < 21:
        print("Bonne soirée, Monsieur")
        speak("Bonne soirée, Monsieur")

    else:
        print("Bonne nuit, Monsieur")
        speak("Bonne nuit, Monsieur")

if __name__ == "__main__":
    nom = input("donner votre nom : ")
    wishings()
    query = commands().lower()
    if 'heure' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        print(strTime)
        speak(f"Monsieur {nom}, il est {strTime}")

    elif 'ouvrir firefox' in query:
        speak("Ouverture de l'application Firefox Monsieur...")
        os.startfile('C:/Program Files/Mozilla Firefox/firefox.exe')

    elif 'chercher' in query:
        keyword = query.split('chercher')[-1].strip()
        if 'youtube' in query:
            speak(f"Recherche de {keyword} sur YouTube...")
            pywhatkit.playonyt(keyword)
        elif 'wikipedia' in query:
            speak(f"Recherche de {keyword} sur Wikipedia...")
            try:
                results = wikipedia.summary(keyword, sentences=2)
                speak(f"Selon Wikipedia, {results}")
                print(results)
            except:
                speak("Désolé, je n'ai eu de résultats pour cette recherche")
                print("Aucun résultat trouvé...")
        else:
            speak("Désolé, je n'ai pas compris sur quel canal ous voulez chercher. Précisez si cest  'YouTube' ou 'Wikipedia'")
