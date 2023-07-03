import pyttsx3                                  # pip install pyttsx3
import webbrowser as web
import time
import keyboard
import smtplib                                  # pip install secure-smtplib
import os
from PIL import Image
import datetime as dt
import requests
# from os import startfile
# from pyautogui import click
# from keyboard import press
# from keyboard import write
# from time import sleep

Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
Assistant.setProperty('voice', voices[2].id)
Assistant.setProperty('rate', 200)

# Speak
def speak(text):
    print("   ")
    Assistant.say(text)
    print(f" {text}")
    print("   ")
    Assistant.runAndWait()


# Whatsapp.
def whatsapp_msg(number, message):
    try:
        num = '+91' + number
        open_chat = "https://web.whatsapp.com/send?phone=" + num
        web.open(open_chat)
        time.sleep(15)
        keyboard.write(message)
        time.sleep(1)
        keyboard.press('enter')
    except:
        speak('Try Again...')

def whatsapp_grp(group_id, message):
    try:
        open_chat = "https://web.whatsapp.com/accept?code=" + group_id
        web.open(open_chat)
        time.sleep(15)
        keyboard.write(message)
        time.sleep(1)
        keyboard.press('enter')
    except:
        speak('Try Again...')

'''def whatsapp():
    speak('Tell me the name of the person.')
    name = takecommand()
    #elif 'time' in query:
    #    time = datetime.datetime.now().strftime('%I:%M %p')
    #    print(time)
    #    speak('Current Time Is ' + time)


    if 'vinita' in name:
        speak('Tell me the message.')
        msg = takecommand()
        speak('Tell me the time')
        speak('Hour')
        hour = int(takecommand())
        speak('Minutes')
        min = int(takecommand())
        pywhatkit.sendwhatmsg('+916260585621', msg, hour, min, 20)
        speak('Whats app message send.')

    elif 'ritesh' in name:
        speak('Tell me the message.')
        msg = takecommand()
        speak('Tell me the time')
        speak('Hour')
        hour = int(takecommand())
        speak('Minutes')
        min = int(takecommand())
        pywhatkit.sendwhatmsg("+918817956908", msg, hour, min, 20)
        speak('Whats app message send.')

    else:
        speak('Tell me the phone number.')
        phone = int(takecommand())
        ph = '+91' + phone
        speak('Tell me the message.')
        msg = takecommand()
        speak('Tell me the time')
        speak('Hour')
        hour = int(takecommand())
        speak('Minutes')
        min = int(takecommand())
        pywhatkit.sendwhatmsg(ph, msg, hour, min, 20)
        speak('Whats app message send.')
        pywhatkit.sendwhatmsg()'''

# Send Email.
def sendEmail(to, content):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('neerajsolanki271@gmail.com', 'kkji gyqo huwb iqez')
        server.sendmail('neerajsolanki271@gmail.com', to, content)
        server.close()
    except:
        speak('Try Again...')


# My Location
def MyLocation():
    ip_add = requests.get('https://api.ipify.org').text
    url = 'https://get.geojs.io/v1/ip/geo/' + ip_add + '.json'
    geo_q = requests.get(url)
    geo_d = geo_q.json()
    state = geo_d['city']
    country = geo_d['country']
    speak(f'you are now in {state, country}.')

Api_Key = "0Mbokl75mTpQGdcAhLwWeqzkCdALwlu9plyKMyeB"

# Nasa
def NasaNews(Date):
    try:
        speak('Extracting data from NASA')
        url = "https://api.nasa.gov/planetary/apod?api_key=" + str(Api_Key)
        para = {'date':str(Date)}
        r = requests.get(url, params = para)
        Data = r.json()
        Info = Data['explanation']
        Title = Data['title']
        Image_Url = Data['url']
        Image_r = requests.get(Image_Url)
        FileName = str(Date) + '.jpg'
        with open(FileName, 'wb') as f:
            f.write(Image_r.content)
        Path_1 = "C:\\Users\\neera\\PycharmProjects\\Advance Friday 2.0\\" + str(FileName)
        Path_2 = "C:\\Users\\neera\\PycharmProjects\\Advance Friday 2.0\\NasaImageData\\" + str(FileName)
        os.rename(Path_1, Path_2)
        img = Image.open(Path_2)
        img.show()
        speak(f"Title : {Title}")
        speak(f"According to Nasa : {Info}")
        os.remove("C:\\Users\\neera\\PycharmProjects\\Advance Friday 2.0\\NasaImageData\\" + str(FileName))
    except:
        speak('I did not understand can you say it again please')

def Weather():
    try:
        # API_ID = "6bdc65b2712df413f9c8c024944dddb8"

        BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
        API_KEY = "6bdc65b2712df413f9c8c024944dddb8"
        CITY = 'Dewas'

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


'''def Summary(Body):
    name = str(Body)
    url = "https://hubblesite.org/api/v3/glossary/" + str(name)
    r = requests.get(url)
    Data = r.json()
    if len(Data) != 0:
        retur = Data['definition']
        speak(f"According to the Nasa : {retur}")
    else:
        speak("No data available for this, so try again later.")

Summary('earth')'''