import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import random
import pywhatkit as kit
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning.")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("Hello Dear, I'm Roosie. Your Virtual Assistant. Please tell me how may I help you?")       

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User: {query}\n")

    except Exception as e:    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open YouTube' in query:
            webbrowser.open("youtube.com")

        elif 'open Google' in query:
            speak("Sir, What should I search on Google?")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")

        elif 'open Microsoft' in query:
            webbrowser.open("microsoft.com")

        elif 'open whatsapp' in query:
            webbrowser.open("youtube.com")

        elif 'Send WhatsApp Message' in query:
            kit.sendwhatmsg("+918421565366", "Hello! This is Test Message.",2,25)

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play song on youtube' in query:
            speak("Which Song do you like to play?")
            yts = takeCommand().lower()
            kit.playonyt(f"{yts}")

        elif 'open notepad' in query:
            notepad_dir = 'C:\\Windows\\System32\\notepad.exe'
            os.startfile(notepad_dir)

        elif 'open mycomputer' in query:
            comp_dir = 'C:\\Users\\Dhananjay\\Desktop'
            os.startfile(comp_dir)
 
        elif 'play songs from my Local Computer' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak("Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = " "
            os.startfile(codePath)

        elif 'email to amey' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "ameyjojare@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Hello Dear! I am not able to send this email")

        elif 'stop listening' in query:
            speak("Okay Sir, Thanks for Using me. Good Bye!")
            sys.exit()

        speak("Sir, DO you have any other Work?")