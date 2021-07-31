import json
import requests
from pywhatkit import main
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
import instaloader
import pyautogui

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
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

########################################################################################

def news():
    main_url = 'https://newsapi.org/v2/top-headlines?country=in&apiKey=0e1d349cb47a4d0b9abca754ac83b595'

    main_page = requests.get(main_url).json()
    articles = main_page ["articles"]

    head = []
    day = ["first","second","third","fourth","fifth","sixth","seventh","eighth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        speak(f"Today's, {day[1]} news is {head[1]}")

########################################################################################

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

        elif 'open browser' in query:
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

############################################################################################

        elif 'close notepad' in query:
            speak("Okay dear, I'll Close Notepad")
            os.system("taskkill /f /im notepad.exe")

        elif 'news' in query:
            speak("Please wait for a while, as I'll fetch Latest News for you.")
            news()

        elif 'my location' in query or 'where i m' in query:
            speak("Okay Dear, Let me Check...")
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                city = geo_data['city']
                state = geo_data['state']
                country = geo_data['country']
                speak(f"I'm not Sure, but according to your IP Address, we are in {city} city, {state} state, of {country} country")
            except Exception as e:
                speak(f"Oops! Something Went wrong. I'm unable to find your Location in Meantime.")

        elif 'search profile on instagram' in query or 'instagram profile' in query:
            speak("Please Enter Username of Profile")
            insta_id = input("Enter Instagram ID here: ")
            webbrowser.open(f"www.instagram.com/{insta_id}")
            speak(f"Here is the instagram profile of user {insta_id}")
            time.sleep(5)
            speak(f"Do you Like to Download Profile Picture of this Instagram Account?")
            condition = takeCommand().lower()
            if 'yes' in condition:
                mod = instaloader.Instaloader()
                mod.download_profile(name, profile_pic_only=True)
                speak("Vola! It's done. I stored it in our Main Folder")
            else:
                pass
        
        elif 'screenshot' in query:
            speak(f"Please tell me the name you would like to give for this Screenshot")
            ss_n = takeCommand().lower()
            speak(f"Great! Please Hold the screen for Few seconds, I'm taking the screenshot")
            img = pyautogui.screenshot()
            img.save(f"{ss_n}.jpg")
            speak(f"I'm done dear, Screenshot is Saved in Main Folder.")

        '''elif 'calculate' in query:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                speak(f"What you want to calculate? Say like: 2 plus 2")
                print("Listening...")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            my_string = r.recognize_google(audio)
            print(my_string)
            def get_operator_fn(op):
                return {
                    '+' : operator.add
                    '-' : operator.sub

                }'''

        

############################################################################################
        speak("Anything other I can do for you?")