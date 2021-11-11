import winsound
import random
import time
import webbrowser
import urllib.request
import datetime
import subprocess
import requests
import codecs
import os
import json
import re
import ssl
import smtplib
import msvcrt
import sys
import getpass
import platform
from playsound import playsound
from pathlib import Path
from urllib.request import pathname2url
from googlesearch import *
from datetime import date
import math
import numpy as np
from win32api import GetSystemMetrics
import matplotlib.pyplot as plt
import threading
import pyttsx3
import speech_recognition as sr
import pyaudio
import psutil
import asyncio
import python_weather

def ADD(x,y):
    return x+y
def SUB(x,y):
    return x-y
def MUL(x,y):
    return x*y
def DIV(x,y):
    return x/y
def EXP(x,y):
    return math.pow(x,y)
def ROOT(x,y):
    return x**y

x2=10
new=2
res=requests.get("https://ipinfo.io/")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
smtp_server = "smtp.gmail.com"
data=res.json()
city=data['city']
location=data['loc'].split(',')
lat=location[0]
lon=location[1]
port = 0
battery = psutil.sensors_battery()
AR=['I am not sure, maybe I can do a web search?',"Didn't get you, how about a web search?","Nope, not really","I am not able to process this one at the moment, maybe a web search will help"]
AR1=['Hey','Hello','Hi','Howdy','Greetings']
AR2=['Goodbye','Bye','Have a good time','Greetings','Good day']
AR3=["You're welcome!","Welcome","Glad to be of help!","My pleasure!"]
AR4=["I am very good! Thanks for asking!","Great! I am grateful to you for having me asked!","Today's been wonderful"]
r=sr.Recognizer()
currentTime = datetime.datetime.now()
my_system = platform.uname()
inp=f"{my_system.node}"
print("Pymate: Hello there",inp,"how may I help you?")
pyttsx3.speak("Hi there, "+inp+", how may I help you?")
x=2
while x2>0:  
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            print("Recognizing...")
            print("You: ")
            query = r.recognize_google(audio, language ='en-in')
            print(query)

            if query == "hello" or query == "hi" or query == "hai":
                print(random.choice(AR1))
                pyttsx3.speak(random.choice(AR1))

            elif query == "show time" or query == "time now" or query == "time" or query == "what is the time":
                print(time.strftime("%H:%M:%S"))
                if currentTime.hour < 12:
                    print('Pymate: Good morning',inp)
                    pyttsx3.speak("Good morning "+inp+ "now it is "+ time.strftime("%H:%M:%S"))
                elif 12 <= currentTime.hour < 18:
                    print('Pymate: Good afternoon',inp)
                    pyttsx3.speak("Good afternoon "+inp+ "now it is "+ time.strftime("%H:%M:%S"))
                else:
                    print('Pymate: Good evening',inp)
                    pyttsx3.speak("Good evening "+inp+ "now it is "+ time.strftime("%H:%M:%S"))

            elif query == "how are you" or query == "what's up":
                print(random.choice(AR4))
                pyttsx3.speak(random.choice(AR4))
                print("Hope your day goes well!")
                pyttsx3.speak("Hope your day goes well!")

            elif query == "calculator" or query == "math mode":
                try:
                    print("Math mode active!")
                    print('''PyMate can perform the following calculations as of now:
            1: ADDITION
            2: SUBTRACTION
            3: MULTIPLICATION
            4: DIVISION
            5: EXPONENTIAL
            6: ROOT
            \n Please choose one option.''')

                    pyttsx3.speak('PiMate can perform the following calculations as of now')
                    a1=input()
                    if a1 == '1':
                        pyttsx3.speak("ADD MODE")
                        x1 = float(input("Enter a number: "))
                        x2 = float(input("Enter another number: "))
                        print(ADD(x1,x2))

                    elif a1 == '2':
                        pyttsx3.speak("SUBTRACT MODE")
                        x1 = float(input("Enter a number: "))
                        x2 = float(input("Enter another number: "))
                        print(SUB(x1,x2))

                    elif a1 == '3':
                        pyttsx3.speak("MULTIPLICATION MODE")
                        x1 = float(input("Enter a number: "))
                        x2 = float(input("Enter another number: "))
                        print(MUL(x1,x2))
                        
                    elif a1 == '4':
                        pyttsx3.speak("DIVISION MODE")
                        x1 = float(input("Enter a number: "))
                        x2 = float(input("Enter another number: "))
                        print(DIV(x1,x2))

                    elif a1 == '5':
                        pyttsx3.speak("EXPONENTIAL MODE")
                        x1 = float(input("Enter a number: "))
                        x2 = float(input("Enter another number: "))
                        print(EXP(x1,x2))

                    elif a1 == '6':
                        pyttsx3.speak("ROOT MODE")
                        x1 = float(input("Enter a number: "))
                        x2 = float(input("Enter another number: "))
                        print(ROOT(x1,x2))

                    else:
                        print("Invalid input")
                        pyttsx3.speak("Invalid input")
                        continue

                except:
                    print("Math mode exited due to invalid input")
                    pyttsx3.speak("Invalid input exited math mode")
                    continue

            elif query == "date" or query == "today's date" or query == "what is today's date":
                d = date.today()
                d1 = d.strftime("%B %d, %Y")
                print("Today's date is: ",d1)
                pyttsx3.speak("Today's date is: "+d1)

            elif query == "where am I" or query == "location":
                print("You are in "+city)
                pyttsx3.speak("You are in "+city)
                print("Latitude",lat)
                print("Longitude",lon)

            elif query == "weather" or query == "what is the weather":
                async def getweather():
                    client = python_weather.Client(format=python_weather.METRIC)
                    weather = await client.find(city)
                    print("Temperature is:",weather.current.temperature,"degrees")

                    for currentTime in weather.forecasts:
                        print(str(currentTime.date), currentTime.sky_text, currentTime.temperature)
                        
                    await client.close()
                    pyttsx3.speak(f"It is now {weather.current.temperature} degrees centigrade")
                    pyttsx3.speak(f"Weather is: {currentTime.sky_text}") 

                if __name__ == "__main__":
                    loop = asyncio.get_event_loop()
                    loop.run_until_complete(getweather())


            elif query == "open YouTube" or query == "YouTube":
                pyttsx3.speak("Now opening YouTube")
                webbrowser.open("https://youtube.com/")

            elif query == "send mail" or query == "mail":
                print("Enter the mailing address of the person: ")
                pyttsx3.speak("Okay, "+inp+", enter mailing address of the person")
                y=input()
                y1=re.findall("[a-z A-Z 0-9 :-@ *-/]",y)
                if y1:
                    print("Valid e-mail")
                    time.sleep(1)
                    print("Enter your valid e-mail address: ")
                    pyttsx3.speak("Now, enter your e-mail address")
                    mymail=input()
                    print("Your email address seems to be in order. Enter your password: ")
                    pyttsx3.speak("Okay, "+inp+", Now enter password")
                    y2 = getpass.getpass()
                    if mymail and y2:
                        print("Access granted")
                        pyttsx3.speak("Access granted!")
                    else:
                        print("Try again")
                        pyttsx3.speak("Wrong Password, Try Again")
                        break
                    z = input("Enter context: ")
                    y3 = input("So you want to send mail to " + y + "? Y/N: ")
                    if y3 == "Y":
                        print("Sending mail")
                        context = ssl.create_default_context()
                        with smtplib.SMTP(smtp_server, port) as server:
                            server.ehlo()
                            server.starttls(context=context)
                            server.ehlo()
                            server.login(mymail, y2)
                            server.sendmail(mymail, y, z)
                        print("Mail sent")
                        pyttsx3.speak("Mail sent successfully!")
                    else:
                        continue

            elif query == "device details":               
                my_system = platform.uname()
                print("Okay, so the following data shows the details of your computer: ")
                time.sleep(1)
                print(f"System: {my_system.system}")
                pyttsx3.speak(f"System: {my_system.system}")
                print(f"Node Name: {my_system.node}")
                pyttsx3.speak(f"Node Name: {my_system.node}")
                print(f"Release: {my_system.release}")
                #pyttsx3.speak(f"System: {my_system.system}")
                print(f"Version: {my_system.version}")
                #pyttsx3.speak(f"System: {my_system.system}")
                print(f"Machine: {my_system.machine}")
                pyttsx3.speak(f"Machine: {my_system.machine}")
                print(f"Processor: {my_system.processor}")
                pyttsx3.speak(f"Processor: {my_system.processor}")
                print(f"Architectural Details: {platform.architecture()}")
                #pyttsx3.speak(f"System: {my_system.system}")
                print("Screen Resolution: WIDTH * HEIGHT: ", GetSystemMetrics(0),"X", GetSystemMetrics(1))
                if battery.power_plugged:
                    print("Battery charging at",battery.percent,"%")
                    pyttsx3.speak("Battery charging at, ")
                    pyttsx3.speak(str(battery.percent) +"%")
                else:
                    print("Running on battery",battery.percent,"%")
                    pyttsx3.speak("Running on battery at, ")
                    pyttsx3.speak(str(battery.percent) +"%")

            elif query == "create a file" or query == "file handle":
                print("Enter a file name:\n")
                pyttsx3.speak("Enter a file name: ")
                a=input()
                file_exists=os.path.isfile(a)

                if file_exists:
                    ans=input("File already exists. A)ppend OR E)rase OR C)ancel: ")
                    pyttsx3.speak("The entered file already exists. Enter any one of the given choices: ")
                    if ans == 'a' or ans == 'A':
                        file_status=open(a,"a+")
                        file_content=input("Enter contents of "+a+":\n")
                        file_status.write("\n")
                        file_status.write("\n")
                        file_status.write(file_content)
                        file_status.close()

                    if ans == 'e' or ans =='E':
                        os.remove(a)
                else:
                    file_status=open(a,'w+')
                    file_content=input("Enter contents of "+a+":\n")
                    file_status.write("\n")
                    file_status.write("\n")
                    file_status.write(file_content)
                    file_status.close()

            elif query == "who am I" or query == "what is my name":
                print("You are",inp)
                pyttsx3.speak("You are, "+inp)

            elif query == "about" or query == "who are you":
                print("That's me, Pymate V1.0 tested and developed by Kapilesh Simha")
                pyttsx3.speak("That's me, Pymate Version 1.0, tested and developed by Kapilesh Simha")
                time.sleep(1)
                print("Do you want to know more about Kapilesh Simha? Y/N: ")
                pyttsx3.speak("Want to know more about Kapilesh Simha?")
                aw=input()
                if aw=="Y":
                    pyttsx3.speak("Thank you for asking about Kapilesh, here you go")
                    url = "file:C:\Program Files\Pymate\Pymate Extras\kaps.html"
                    webbrowser.open(url,new=new)

                else:
                    continue
                    
            elif query == "thank you" or query == "thanks":
                print(random.choice(AR3))
                pyttsx3.speak(random.choice(AR3))

            elif query == "goodbye" or query == "bye bye" or query == "exit":
                print(random.choice(AR2))
                pyttsx3.speak(random.choice(AR2))
                exit()
            else:
                print("Pymate: ",random.choice(AR))
                pyttsx3.speak(random.choice(AR))
                time.sleep(1)
                aq=input("Do a web search? Y/N: ")
                if aq=="Y":
                    pyttsx3.speak("Searching for "+query)
                    chrome_path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
                    for url in search(query, tld="co.in", num=1, stop = 1, pause = 2):
                        webbrowser.open("https://google.com/search?q=%s" % query)
 
        except Exception as e:
            print(e)
            print("Unable to Recognize your voice.")

