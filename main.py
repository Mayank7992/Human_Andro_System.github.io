import datetime
import os
import webbrowser
import pyttsx3
import speech_recognition as sr
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        speak("Good Morning")

    elif(hour>=12 and hour<18):
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("I am Mayank AI Sir,Mam. Please tell me how may I help you")

def takeCommand():
    # It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

# def sendEmail(to,content):

if __name__ == '__main__':
    wishMe()
    # while True:
    if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("Wikipedia","")
            results = wikipedia.summary(query,sentences = 2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'how are you' in query:
            speak("I am fine what about you")

        elif 'good food' in query:
            speak("Ok,for good foods never eat fast food try to eat fruits like apple orange banana and many more"
                  " thank you")

        elif 'open gpt' in query:
            webbrowser.open("chatgpt.com")

        elif 'open gemini' in query:
            webbrowser.open("bard.google.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favourite songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,Mam the time is {strTime} thanks for asking me")
            print(strTime)

        elif 'open browser' in query:
            chrome_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"
            os.startfile(chrome_path)