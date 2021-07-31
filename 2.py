import wikipedia
import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import os
import smtplib
import pyjokes
import pywhatkit as kit
import random
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("Hello Dear, I'm Roosie. Your Virtual Assistant. Please tell me how can I help you")       

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('notabletoday@gmail.com', '24dhananjay')
    server.sendmail('notabletoday@gmail.com', to, content)
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
        elif 'send email' in query:
            try:  
                speak("What should I say?")
                content = takeCommand()
                to = "ameyjojare@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry dear. I am unable to send this email")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open whatsapp' in query:
            webbrowser.open("web.whatsapp.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")

        elif 'open moodle' in query:
            webbrowser.open("https://lms.jspmrscoe.edu.in/login/index.php")

        elif 'open easy pariksha' in query:
            webbrowser.open("https://epjspm.edupluscampus.com/")

        elif 'open cricbuzz' in query:
            webbrowser.open("cricbuzz.com")

        elif 'open google' in query:
            speak("dear, What should I search on Google?")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")

        elif 'play song on youtube' in query:
            speak("Which Song do you like to play?")
            yts = takeCommand().lower()
            kit.playonyt(f"{yts}")

        elif 'open notepad' in query:
            notepad_dir = 'C:\\Windows\\System32\\notepad.exe'
            os.startfile(notepad_dir)

        elif 'close notepad' in query:
            speak("Okay dear, I'll Close Notepad")
            os.system("taskkill /f /im notepad.exe")

        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'joke' in query:
            print(pyjokes.get_joke())
            speak(pyjokes.get_joke())
            

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open whatsapp desktop' in query:
            webbrowser.open("whatsappdesktop.com")         

        elif 'play songs from my local computer' in query:
            music_dir = 'D:\\songs'
            songs = os.listdir(music_dir)
            print(songs)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\AMEY JOJARE\\AppData\\Local\\Programs\\Microsoft VS Code"
            os.startfile(codePath)

        elif 'stop listening' in query:
            speak("Okay dear, Thanks for Using me. Good Bye!")
            sys.exit()

        speak("okay, dear do you have any other Work?")
