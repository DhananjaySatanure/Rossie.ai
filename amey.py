import wikipedia   #amey
import pyjokes     #amey 
import pywhatkit as kit   #amey
import pyautogui   #mehraj
import os         #mehraj
import pyttsx3    #sam
import webbrowser  #sam
import sys     #sam
import datetime    #roshani
import smtplib    #roshani
import requests   #dhanu
import speech_recognition as sr #dhanu
from pywikihow import search_wikihow   #dhanu

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
    server.login('jojareamey2@gmail.com', 'abcd@1234')
    server.sendmail('jojareamey2@gmail.com', to, content)
    server.close()

def news():
    main_url = 'https://newsapi.org/v2/top-headlines?country=in&apiKey=0e1d349cb47a4d0b9abca754ac83b595'

    main_page = requests.get(main_url).json()
    articles = main_page ["articles"]

    head = []
    day = ["first","second","third","fourth","fifth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        speak(f"Today's, {day[i]} news is {head[i]}")


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
        elif 'send mail' in query:
            try:
                speak("To whom you want to send?")
                email_id = input("Enter Recipient Email ID here: ")
                speak("What should I say?")
                content = takeCommand()
                to = {email_id}
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
         

        elif 'play music' in query:
            music_dir = 'D:\\songs'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[5]))

        elif 'screenshot' in query:
            speak(f"Please tell me the name you would like to give for this Screenshot")
            ss_n = takeCommand().lower()
            speak(f"Great! Please Hold the screen for Few seconds, I'm taking the screenshot")
            img = pyautogui.screenshot()
            img.save(f"{ss_n}.jpg")
            speak(f"I'm done dear, Screenshot is Saved in Main Folder.")

        elif 'search profile on instagram' in query or 'instagram profile' in query:
            speak("Please Enter Username of Profile")
            insta_id = input("Enter Instagram ID here: ")
            webbrowser.open(f"www.instagram.com/{insta_id}")

        elif 'news' in query:
            speak("Please wait for a while, as I'll fetch Latest News for you.")
            news()
            

        elif 'activate how to do mode' in query:
            speak(f"How to Do mode is Activated. Please Tell me what you want to do?")            
            how = takeCommand()
            try:
                if "deactivate" in how:
                    speak(f"Okay Dear, How to Do mode is Deactivated")
                    break
                else:
                    max_results = 1
                    how_to = search_wikihow(how, max_results)
                    assert len(how_to) == 1
                    how_to[0].print()
                    speak(how_to[0].summary)
            except Exception as e:
                speak(f"Sorry Dear, I'm not able to find this please try something different.")



        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\AMEY JOJARE\\AppData\\Local\\Programs\\Microsoft VS Code"
            os.startfile(codePath)

        elif 'stop listening' in query:
            speak("Okay dear, Thanks for Using me. Good Bye!")
            sys.exit()
            
        elif "www" in query or "com" in query:
            try:
                final = str(final)
                sp = str(final.replace("open",""))
                sp = str(sp.replace(" ",""))
                sp = str(sp.replace("www.",""))
                sp = str(sp.replace(".com",""))
                sp1 = "opening "+sp+".com"
                speak(sp1)
                chrome_path = "C:\Program Files\Google\Chrome\Application\Chrome.exe"
                webbrowser.register("chrome", None, webbrowser.BackgroundBrowser(chrome_path))
                final = "https://www."+sp+".com"
                print(final)
                webbrowser.get("chrome").open_new_tab(final)
            except:
                speak("having some internal issue")

        speak("okay, dear do you have any other Work?")
