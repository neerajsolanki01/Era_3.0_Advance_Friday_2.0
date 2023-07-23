import speech_recognition as sr                         # pip install SpeechRecognition
#  From Archived: Unofficial Windows Binaries for Python Extension Packages " https://www.lfd.uci.edu/~gohlke/pythonlibs/ "
#  pip install .\PyAudio-0.2.11-cp38-cp38-win_amd64.whl
import pyttsx3                                          # pip install pyttsx3
# import time
# from time import sleep
import datetime
import datetime as dt
import pywhatkit                                        # pip install pywhatkit
import keyboard                                         # pip install keyboard
from keyboard import press_and_release
from keyboard import press
import random
import wikipedia                                        # pip install wikipedia
import webbrowser
# import webbrowser as web
import os
# from playsound import playsound
# import mss
# import cv2
from requests import get                                # pip install requests
# import numpy as np
import pyautogui                                        # pip install PyAutoGUI
# import smtplib
import pyjokes                                          # pip install pyjokes
from pywikihow import search_wikihow                    # pip install pywikihow
import requests
from bs4 import BeautifulSoup                           # pip install beautifulsoup4
# import pyscreenshot as ImageGrab
# from googletrans import Translator
import features
# import wolframalpha                                      # pip install wolframalpha
# import chatbot
# from PyDictionary import PyDictionary as Dict


Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
Assistant.setProperty('voice', voices[5].id)
Assistant.setProperty('rate', 200)

Assistant.say('Hey, I Am Friday 3.0, Your personal virtual assistant.')
Assistant.runAndWait()


# Speak
def speak(text):
    print("   ")
    Assistant.say(text)
    print(f" {text}")
    print("   ")
    Assistant.runAndWait()

# Take Command.
def takecommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        # speak('Listening...')
        command.pause_threshold = 1
        audio = command.listen(source, 0, 4)

        try:
            print('Recognizing...')
            # speak('Recognizing...')
            query = command.recognize_google(audio, language='en-in')
            print(f"user said: {query}")

        except:
            return "none"
        return query.lower()

# Take Command In Hindi.
def takecommand_hindi():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        # speak('Listening...')
        command.pause_threshold = 1
        audio = command.listen(source, 0, 4)

        try:
            print('Recognizing...')
            # speak('Recognizing...')
            query = command.recognize_google(audio, language='hi')
            print(f"user said: {query}")

        except:
            return "none"
        return query.lower()

# To Wish Me.
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour <= 11:
        speak('Good Morning')
    elif 12 <= hour <= 15:
        speak('Good Afternoon')
    else:
        speak('Good Evening')


def TaskExe():
    wishMe()

    # Open Apps
    def OpenApps():

        if 'notepad' in query:
            path = 'C:\\Windows\\System32\\notepad.exe'
            os.startfile(path)
            speak('Opening Notepad.')

        elif 'microsoft word' in query:
            path = 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\word'
            os.startfile(path)
            speak('Opening MS Word')

        elif 'command prompt' in query:
            os.system('start cmd')
            speak('Opening Command Prompt.')

    # Close Application.
    def CloseApps():

        if 'notepad' in query:
            os.system("TASKKILL /F /im notepad.exe")

        elif 'microsoft word' in query:
            os.system("TASKKILL /F /im WINWORD.EXE")

        elif 'command prompt' in query:
            os.system("TASKKILL /F /im cmd.exe")

    # Speedtest
    def SpeedTest():
        import speedtest
        speak('I am checking internet speed, wait a minute sir...')
        speed = speedtest.Speedtest()
        downloading = speed.download()
        correctDown = int(downloading / 800000)
        uploading = speed.upload()
        correctUpload = int(uploading / 800000)

        if 'downloading' in query:
            speak(f"The downloading speed is {correctDown} mbps")
        elif 'uploading' in query:
            speak(f"The uploading speed is {correctUpload} mbps")
        else:
            speak(f"The downloading speed is {correctDown} mbps and The uploading speed is {correctUpload} mbps")


    # Alarm Not Working.
    '''def Alarm(query):
        TimeHere = open('C:\\Users\\neera\\PycharmProjects\\Advance Friday 2.0\\Alarm_Data.txt', 'a')
        TimeHere.write(query)
        os.startfile("C:\\Users\\neera\\PycharmProjects\\Advance Friday 2.0\\Alarm_Clock.py")'''

    '''# Wolfram Alpha.
    def Wolfram(query):
        api_key = "QW5TUJ-HJ6E4GHYR9"
        requester = wolframalpha.Clint(api_key)
        requested = requester.query(query)

        try:
            Answer = next(requested.results).text
            return Answer
        except:
            speak('No Data found related to it.')
    def Calculator(query):
        term = str(query)
        term = term.replace('calculate', '')
        term = term.replace('multiply', '*')
        term = term.replace('plus', '+')
        term = term.replace('minus', '-')
        term = term.replace('divide', '/')
        Final = str(term)
        try:
            result = Wolfram(Final)
            speak(result)
        except:
            speak('No Data found related to it.')
    def Temperature(query):
        Temp = str(query)
        Temp = Temp.replace("what is the temperature in ", " ")
        temp_query = str(Temp)
        if 'temperature' in temp_query:
            speak('At where are you.')
            cm = takecommand().lower()
            ans = f 'temperature in {cm}'
            answer = Wolfram(ans)
            speak(f'{ans} is {answer}.')
        else:
            var = "temperature in " + temp_query
            answer1 = Wolfram(var)
            speak(f'{var} is {answer1}.')'''






# While True Execution All Statement.
    while True:
        query = takecommand()

        # Play anything on YouTube.
        if 'play' in query:
            song = query.replace('play', '')
            speak('Playing...' + song)
            pywhatkit.playonyt(song)
            speak('Playing...')
            print('Playing...')

        # Time, Date, Temperature
        elif 'time' in query:
            time = datetime.datetime.now().strftime('%I:%M %p')
            print(time)
            speak('Current Time Is ' + time)

        elif 'date' in query:
            date = datetime.datetime.now().strftime('%d-%m-%Y')
            print(date)
            speak('Today date is ' + date)

        elif 'temperature' in query:
            try:
                speak('At where are you.')
                cm = takecommand().lower()
                query = query.replace('in', ' ')
                url = f"https://www.google.com/search?q=temperature+in+{cm}"
                r = requests.get(url)
                data = BeautifulSoup(r.text, "html.parser")
                temp = data.find("div", class_="BNeawe").text
                speak(f"current temperature in {cm} is {temp}")
                print(f"current temperature in {cm} is {temp}")
            except:
                speak('Sorry, i did not understand the city name.')

        elif 'weather' in query:
            try:

                BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
                API_KEY = "893850988986987769ljjhsvl ji88977 "
                speak('At where are you.')
                CITY = takecommand().lower()
                query = query.replace('in', ' ')
                # CITY = 'Dewas'

                def kelvin_celsius(kelvin):
                    celcius = kelvin - 273.15
                    return celcius

                url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
                response = requests.get(url).json()

                temp_kelvin = response['main']['temp']
                temp_celsius = kelvin_celsius(temp_kelvin)
                feels_like_kelvin = response['main']['feels_like']
                feels_like_celsius = kelvin_celsius(feels_like_kelvin)
                humidity = response['main']['humidity']
                pressure = response['main']['pressure']
                visibility = response['visibility'] / 1000
                # rain = response['weather']['rain']
                # clouds = response['main']['clouds']
                wind_speed = response['wind']['speed']
                description = response['weather'][0]['description']
                sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
                sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])

                print(f"Temperature in {CITY} is : {temp_celsius:.2f}ºCelcius")
                speak(f"Temperature in {CITY} is : {temp_celsius:.2f}ºCelcius")

                print(f"Temperature in {CITY} feels like : {feels_like_celsius:.2f}ºCelcius")
                speak(f"Temperature in {CITY} feels like : {feels_like_celsius:.2f}ºCelcius")

                print(f"Humidity in {CITY} is : {humidity}% ")
                speak(f"Humidity in {CITY} is : {humidity}% ")

                print(f"Pressure in {CITY} is : {pressure} hecto Pascals or millibars ")
                speak(f"Pressure in {CITY} is : {pressure} hecto Pascals or millibars ")

                print(f"Visibility in {CITY} is : {visibility} kilometer ")
                speak(f"Visibility in {CITY} is : {visibility} kilometer ")

                print(f"Wind Speed in {CITY} is : {wind_speed} kilometer per hour ")
                speak(f"Wind Speed in {CITY} is : {wind_speed} kilometer per hour ")

                print(f"General Weather in {CITY} is : {description} ")
                speak(f"General Weather in {CITY} is : {description} ")

                print(f"Sun Rises in {CITY} at {sunrise_time} local time")
                speak(f"Sun Rises in {CITY} at {sunrise_time} local time")

                print(f"Sun Set in {CITY} at {sunset_time} local time ")
                speak(f"Sun Set in {CITY} at {sunset_time} local time ")
            except:
                speak('Sorry, i did not understand the city name.')


        # Open Application
        elif 'open notepad' in query:
            OpenApps()
        elif 'open microsoft word' in query:
            OpenApps()
        elif 'open command prompt' in query:
            OpenApps()
        elif 'open browser' in query:
            path = 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe'
            os.startfile(path)
            speak('Opening Microsoft Edge Browser.')
        elif 'open chrome' in query:
            path = 'C:\\Users\\Public\\Desktop\\Google Chrome.lnk'
            os.startfile(path)
            speak('Opening Chrome Browser.')
        elif 'instagram' in query:
            webbrowser.open('www.instagram.com')
            speak('Opening Instagram.')

        # Close Application.
        elif 'close notepad' in query:
            CloseApps()
        elif 'close microsoft word' in query:
            CloseApps()
        elif 'close command prompt' in query:
            CloseApps()
        elif 'close browser' in query:
            os.system("TASKKILL /F /im msedge.exe")
        elif 'close chrome' in query:
            os.system("TASKKILL /F /im chrome.exe")
            speak('Close Chrome Browser')

        # Screenshot.
        elif 'screenshot' in query:
            speak('Ok, What should i name that file')
            path = takecommand()
            path1name = path + ".png"
            path1 = "C:\\Image\\Screenshot\\" + path1name
            image = pyautogui.screenshot()
            image.save(path1)
            os.startfile("C:\\Image\\Screenshot")
            speak("Your Screenshot is here.")

        # IP Address.
        elif 'ip address' in query:
            ip = get('https://api.ipify.org').text
            speak(f'your IP address is {ip}')

        # Internet Speed
        elif 'internet speed' in query:
            SpeedTest()
        elif 'downloading speed' in query:
            SpeedTest()
        elif 'uploading speed' in query:
            SpeedTest()


        # Music
        elif 'music' in query:
            music_dir = 'C:\\Music\\My Favorite Songs'
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))
            speak('Playing Music...')


        # Alarm.
        # elif 'set alarm' in query:
        #    Alarm(query)

        # Wikipedia.
        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=4)
            speak(results)
            print(results)

        # Search on google with image.
        elif 'search' in query:
            import wikipedia as googleScrap
            query = query.replace('search', ' ')
            query = query.replace('What is ', ' ')
            pywhatkit.search(query)
            try:
                result = googleScrap.summary(query, 2)
                speak(result)
            except:
                return "none"

        # Google Search.
        elif 'google' in query:
            speak('What should i search on google.')
            cm = takecommand().lower()
            webbrowser.open(f'{cm}')


        # How to make
        elif 'how to' in query:
            speak("Getting data from the internet")
            op = query.replace("friday", " ")
            max_result = 1
            how_to_func = search_wikihow(op, max_result)
            assert len(how_to_func) == 1
            how_to_func[0].print()
            speak(how_to_func[0].summary)


        # Website.
        elif 'website' in query:
            speak('Tell me the name of website.')
            name = takecommand()
            web = 'https://www.' + name + '.com'
            webbrowser.open(web)
            speak('Opening...')


        # YouTube Search
        elif 'youtube search' in query:
            speak('What should i search on youtube.')
            cm = takecommand().lower()
            web = 'https://www.youtube.com/results?search_query=' + cm
            webbrowser.open(f'{web}')
            speak(cm)


        # Reminder
        elif 'remind me' in query:
            remembermsg = query.replace("remind me", " ")
            speak('You tell me to remind you :'+remembermsg)
            remember = open('data.text', 'w')
            remember.write(remembermsg)
            remember.close()
        elif 'remember' in query:
            remember = open('data.text', 'r')
            speak('You tell me to remind you:' + remember.read())


        # Joke.
        elif 'joke' in query:
            speak(pyjokes.get_joke())

        # Automate Browser
        elif 'new tab' in query:
            press_and_release('ctrl + t')
        elif 'close tab' in query:
            press_and_release('ctrl + w')
        elif 'new window' in query:
            press_and_release('ctrl + n')
        elif 'history' in query:
            press_and_release('ctrl + h')
        elif 'download' in query:
            press_and_release('ctrl + j')
        elif 'bookmark' in query:
            press_and_release('ctrl + d')
            press('enter')
        elif 'incognito' in query:
            press_and_release('Ctrl + Shift + n')
        elif 'switch tab' in query:
            Tab = query.replace('switch tab', '')
            tab = Tab.replace('to', '')
            num = tab
            kk = f'ctrl + {num}'
            press_and_release(kk)
        elif 'open' in query:
            name = query.replace("open", "")
            Name = str(name)
            if 'youtube' in Name:
                webbrowser.open("https://www.youtube.com/")
            elif 'instagram' in Name:
                webbrowser.open("https://www.instagram.com/")
            else:
                string = "https://" + Name + ".com"
                string2 = string.replace(" ", "")
                string3 = string2.replace("  ", "")
                webbrowser.open(string3)


        # Automate YouTube
        elif 'pause' in query:
            keyboard.press('space bar')
        elif 'resume' in query:
            keyboard.press('space bar')
        elif 'restart' in query:
            keyboard.press('0')
        elif 'mute' in query:
            keyboard.press('m')
        elif 'skip' in query:
            keyboard.press('l')
        elif 'back' in query:
            keyboard.press('j')
        elif 'full screen' in query:
            keyboard.press('f')
        elif 'film screen' in query:
            keyboard.press('t')
        elif 'theater mode' in query:
            keyboard.press('t')
        elif 'mute' in query:
            keyboard.press('m')
        elif 'unmute' in query:
            keyboard.press('m')
        elif 'subtitle' in query:
            keyboard.press('c')
        elif 'caption' in query:
            keyboard.press('c')
        elif 'increase volume' in query:
            keyboard.press('up arrow')
        elif 'decrease volume' in query:
            keyboard.press('down arrow')
        elif 'increase speed' in query:
            press_and_release('shift + .')
        elif 'search box' in query:
            keyboard.press('/')
            speak('what i search')
            search = takecommand()
            keyboard.write(search)
            keyboard.press('enter')
        elif 'decrease speed' in query:
            press_and_release('shift + ,')
        elif 'previous' in query:
            press_and_release('shift + p')
        elif 'next' in query:
            press_and_release('shift + n')


        # Automate Windows
        elif 'close app' in query:
            press_and_release('Alt + F4')
        elif 'setting' in query:
            press_and_release('windows + i')
        elif 'home screen' in query:
            press_and_release('windows + m')
        elif 'minimize' in query:
            press_and_release('windows + m')


        # NASA
        elif 'space news' in query:
            speak('Tell me the date in the format of; year and month and date. For news extracting process')
            Date1 = takecommand()
            Date = Date1.replace(" ", "")
            Date = Date.replace("  ", "")
            Date = Date.replace(" ", "-")
            Date = Date.replace("   ", "-")
            Date = Date.replace("and", "-")
            Date = Date.replace("and", "-")
            Date = Date.replace(" and ", "-")
            from features import NasaNews
            NasaNews(Date)

        # Whatsapp automate
        elif 'whatsapp message' in query:
            query = query.replace("friday", "")
            query = query.replace("send", "")
            query = query.replace("whatsapp message", "")
            query = query.replace("to", "")
            name = query
            if 'vinita' in name:
                num = "626**********"
                speak(f"What's the message for {name}")
                mess = takecommand()
                features.whatsapp_msg(num, mess)
            elif 'papa' in name:
                num = "700**********"
                speak(f"What's the message for {name}")
                mess = takecommand()
                features.whatsapp_msg(num, mess)
            elif 'neeraj' in name:
                num = "7089*********"
                speak(f"What's the message for {name}")
                mess = takecommand()
                features.whatsapp_msg(num, mess)
            elif 'ritesh' in name:
                num = "8817*********"
                speak(f"What's the message for {name}")
                mess = takecommand()
                features.whatsapp_msg(num, mess)
            elif 'friend' in name:
                gro = "FzSPRlptL5DIDHSpphvgNWy"
                speak(f"What's the message for {name}")
                mess = takecommand()
                features.whatsapp_grp(gro, mess)

            elif 'data' in name:
                gro = "IBOQSwzgucqIxxUtrIqSS0hg"
                speak(f"What's the message for {name}")
                mess = takecommand()
                features.whatsapp_grp(gro, mess)


        # Email
        elif 'email to neeraj' in query:
            try:
                speak('What should i say.')
                content = takecommand().lower()
                to = 'solankineeraj@gmail.com'
                features.sendEmail(to, content)
                speak('Email Send')

            except Exception as e:
                print(e)
                speak('Email Not Send')

        elif 'email to vinita' in query:
            try:
                speak('What should i say.')
                content = takecommand().lower()
                to = 'vinitasolanki@gmail.com'
                features.sendEmail(to, content)
                speak('Email Send')

            except Exception as e:
                print(e)
                speak('Email Not Send')

        # Fun Part.
        elif 'are you single' in query:
            speak('I am in a relationship with the, internet or a wifi.')
        elif 'what are you doing' in query:
            speak('I am talking with you Dear.')

        # Exit Part.
        elif 'break' in query:
            speak('Ok sir, you can call me anytime.')
            break
        elif 'exit' in query:
            speak('Thanks for using me , have a good day...')
            exit()
        elif 'stop' in query:
            speak('Thanks for using me , have a good day...')
            exit()
        elif 'not now' in query:
            speak('Thanks for using me , have a good day...')
            exit()

        '''else:
            answer = chatbot.ChatterBot(query)
            speak(answer)'''


TaskExe()
