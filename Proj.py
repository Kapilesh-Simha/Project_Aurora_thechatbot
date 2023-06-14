import winsound
import random
import time
import webbrowser
import urllib.request
import datetime
import subprocess
import requests
import calendar
import codecs
import os
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
import threading
import pyttsx3
import speech_recognition as sr
import psutil
import python_weather
import wmi
import ctypes
import pyjokes
import asyncio
import wikipedia
import pyaudio
from win32api import GetSystemMetrics

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

counter = 0
x2=10
new=2
c = wmi.WMI()    
my_sys = c.Win32_ComputerSystem()[0]
res=requests.get("https://ipinfo.io/")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
data=res.json()
city=data['city']
location=data['loc'].split(',')
lat=location[0]
lon=location[1]
port = 0
cy=datetime.datetime.now().year
battery = psutil.sensors_battery()
AR=['I am sorry, my responses are limited, maybe I can do a web search?',"Didn't get you, how about a web search?","Nope, not really","I am not able to process this one at the moment, maybe a web search will help"]
AR1=['Hey','Hello','Hi','Howdy','Greetings']
AR2=['Goodbye','Bye','Have a good time','Greetings','Good day','Bye Bye']
AR3=["You're welcome!","Welcome","Glad to be of help!","My pleasure!"]
AR4=["I am very good! Thanks for asking!","Great! I am grateful to you for having me asked!","Today's been wonderful"]
r=sr.Recognizer()
currentTime = datetime.datetime.now()
my_system = platform.uname()
inp=f"{my_system.node}"
x=2
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Listening...")
    audio = r.listen(source)
    q1=""
    q1 = r.recognize_google(audio, language ='en-in')
    try:
        print("Recognizing...")
        print("You: ")
        print(q1)
        if "hi Aurora" or "hello Aurora" or "hi" in q1:
            if currentTime.hour<12:
                print("AURORA: Good morning",inp,"how may I help you?")
                pyttsx3.speak("Good morning, "+inp+", how may I help you?")

            elif 12<=currentTime.hour<18:
                print("AURORA: Good afternoon",inp,"how may I help you?")
                pyttsx3.speak("Good afternoon, "+inp+", how may I help you?")

            else:
                print("AURORA: Good evening",inp,"how may I help you?")
                pyttsx3.speak("Good evening, "+inp+", how may I help you?")

            a=input()

            while x2>0:
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    print("\n\nListening...")
                    audio = r.listen(source)
                    query=""
                try:
                    print("Recognizing...")
                    print("You: ")
                    query = r.recognize_google(audio, language ='en-in')
                    print(query)

                    if query == "hello" or query == "hi" or query == "hai":
                        print(random.choice(AR1))
                        pyttsx3.speak(random.choice(AR1))

                        ni=input("Press ENTER to continue")

                    elif "time" in query:
                        print(time.strftime("%H:%M:%S"))
                        if currentTime.hour < 12:
                            print('AURORA: Good morning',inp)
                            pyttsx3.speak("Good morning "+inp+ "now it is "+ time.strftime("%H:%M:%S"))
                        elif 12 <= currentTime.hour < 18:
                            print('AURORA: Good afternoon',inp)
                            pyttsx3.speak("Good afternoon "+inp+ "now it is "+ time.strftime("%H:%M:%S"))
                        else:
                            print('AURORA: Good evening',inp)
                            pyttsx3.speak("Good evening "+inp+ "now it is "+ time.strftime("%H:%M:%S"))

                        ni=input("Press ENTER to continue")

                    elif query == "how are you" or query == "what's up":
                        print(random.choice(AR4))
                        pyttsx3.speak(random.choice(AR4))
                        print("How are you?")
                        pyttsx3.speak("How are you?")
                        with sr.Microphone() as source:
                            audio = r.listen(source)
                            q2=""
                            try:
                                print("Recognizing...")
                                print("You: ")
                                q2 = r.recognize_google(audio, language ='en-in')

                            except Exception as e:
                                print("Unable to recognize your voice.")
                                continue
                            
                        if "fine" or "good" or "great" in q2:
                            print("Good to hear from you!")
                            pyttsx3.speak("Good to hear from you!")

                            ni=input("Press ENTER to continue")

                        else:
                            
                            print("Hope your day goes well!")
                            pyttsx3.speak("Hope your day goes well!")

                            ni=input("Press ENTER to continue")

                    elif query=="calculate" or query=="calculator":
                        try:
                            print("Math mode active!")
                            print('''I can perform the following calculations as of now:
                    1: ADDITION
                    2: SUBTRACTION
                    3: MULTIPLICATION
                    4: DIVISION
                    5: EXPONENTIAL
                    6: ROOT
                    \n Please choose one option.''')

                            pyttsx3.speak("I can perform the following calculations as of now")
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

                            ni=input("Press ENTER to continue")

                        except:
                            print("Math mode exited due to invalid input")
                            pyttsx3.speak("Invalid input exited math mode")
                            continue

                            ni=input("Press ENTER to continue")

                    elif "date" in query:
                        d = date.today()
                        d1 = d.strftime("%B %d, %Y")
                        print("Today's date is: ",d1)
                        pyttsx3.speak("Today's date is: "+d1)

                        ni=input("Press ENTER to continue")

                    elif "calendar" in query:
                        print(calendar.calendar(cy))
                        pyttsx3.speak("This is the calendar for "+str(cy))
                        ni=input("Press ENTER to continue")
                        
                    elif query == "where am I" or "location" in query:
                        print("You are in "+city)
                        pyttsx3.speak("You are in "+city)
                        print("Latitude",lat)
                        print("Longitude",lon)
                        ni=input("Press ENTER to continue")

                    elif "Wikipedia" in query or "wikipedia" in query:
                        print("What to search in Wikipedia?")
                        pyttsx3.speak("What to search in Wikipedia?")
                        inp=input()
                        pyttsx3.speak("Searching for "+ inp +"in Wikipedia")
                        print(wikipedia.summary(inp, sentences=4))
                        
                    elif "temperature" in query or "hot" in query or "cold" in query:
                        async def getweather():
                            client = python_weather.Client(format=python_weather.METRIC)
                            weather = await client.find(city)
                            print("Temperature is:",weather.current.temperature,"degrees")
                            pyttsx3.speak("Temperature is:",weather.current.temperature,"degrees")

                    elif query == "open YouTube" or query=="YouTube":
                        pyttsx3.speak("Now opening YouTube")
                        webbrowser.open("https://youtube.com/")
                        ni=input("Press ENTER to continue")

                    elif query == "mute":
                        try:
                            inl=input("Assistant paused...")
                            pyttsx3.speak("Assistant paused")

                        except:
                            continue

                    elif "joke" in query or "fun" in query:
                        My_joke = pyjokes.get_joke(language="en", category="neutral")
                        print(My_joke)
                        pyttsx3.speak(My_joke)
                        ni=input("Press ENTER to continue")

                    elif "device details" in query or "device" in query or "details" in query:
                        my_system = platform.uname()
                        print("Okay, so the following data shows the details of your computer: ")
                        time.sleep(1)
                        print(f"Manufacturer: {my_sys.Manufacturer}")
                        pyttsx3.speak(f"Manufacturer: {my_sys.Manufacturer}")
                        print(f"NumberOfProcessors: {my_sys.NumberOfProcessors}")
                        pyttsx3.speak(f"NumberOfProcessors: {my_sys.NumberOfProcessors}")
                        print(f"Model: {my_sys.SystemFamily}")
                        pyttsx3.speak(f"Model: {my_sys.SystemFamily}")
                        print(f"System: {my_system.system}")
                        pyttsx3.speak(f"System: {my_system.system}")
                        print(f"Architecture: {my_sys.SystemType}")
                        pyttsx3.speak(f"Architecture: {my_sys.SystemType}")
                        print(f"Node Name: {my_system.node}")
                        pyttsx3.speak(f"Node Name: {my_system.node}")
                        print(f"Release: {my_system.release}")
                        print(f"Version: {my_system.version}")
                        print(f"Machine: {my_system.machine}")
                        pyttsx3.speak(f"Machine: {my_system.machine}")
                        print(f"Processor: {my_system.processor}")
                        print(f"Architectural Details: {platform.architecture()}")
                        print("Screen Resolution: WIDTH * HEIGHT: ", GetSystemMetrics(0),"X", GetSystemMetrics(1))
                        if battery.power_plugged:
                            print("Battery charging at",battery.percent,"%")
                            pyttsx3.speak("Battery charging at, "+ str(battery.percent) +"%")
                        else:
                            print("Running on battery",battery.percent,"%")
                            pyttsx3.speak("Running on battery at, "+str(battery.percent) +"%")
                        ni=input("Press ENTER to continue")

                    elif "play song" in query or "play music" in query or "song" in query or "music" in query:
                        print("Which music? ")
                        pyttsx3.speak("Which music to be played?")
                        mus=input()
                        for url in search(mus, tld="co.in", num=1, stop = 1, pause = 2):
                            print("Now playing",mus,"on Youtube Music")
                            pyttsx3.speak("Now playing "+mus+", on Youtube Music")
                            webbrowser.open("https://music.youtube.com/search?q=%s" % mus)
                        ni=input("Press ENTER to continue")

                    elif "battery" in query or "battery percentage" in query:
                        if battery.power_plugged:
                            print("Battery charging at",battery.percent,"%")
                            pyttsx3.speak("Battery charging at",battery.percent,"%")
                        else:
                            print("Running on battery",battery.percent,"%")
                            pyttsx3.speak("Running on battery",battery.percent,"%")
                            continue
                        ni=input("Press ENTER to continue")

                    elif "shutdown" in query or "power off" in query:
                        print("DO YOU REALLY WANT TO SHUT DOWN THE SYSTEM? Y/N\n")
                        pyttsx3.speak("DO YOU REALLY WANT TO SHUT DOWN THE SYSTEM?")
                        q1=input()
                        if q1 == "Y":
                            print("Shutting down!")
                            pyttsx3.speak("Shutting down!")
                            subprocess.call('shutdown /p /f')
                        else:
                            continue
                                                   
                    elif "note" in query:
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

                        ni=input("Press ENTER to continue")

                    elif query == "who am I" or query == "what is my name":
                        print("You are",inp)
                        pyttsx3.speak("You are, "+inp)
                        ni=input("Press ENTER to continue")

                    elif query == "about" or query == "who are you" or query=="what is your name":
                        print("That's me, AURORA, tested and developed by Kapilesh Simha")
                        pyttsx3.speak("That's me, AURORA, tested and developed by Kapilesh Simha")
                        ni=input("Press ENTER to continue")
                            
                    elif query == "thank you" or query == "thanks":
                        print(random.choice(AR3))
                        pyttsx3.speak(random.choice(AR3))
                        ni=input("Press ENTER to continue")
                        
                    elif query == "search YouTube":
                        print("What to search?")
                        pyttsx3.speak("What to search?")

                        inp=input()
                        for url in search(inp, tld="co.in", num=1, stop = 1, pause = 2):
                            print("Now opening",inp,"on Youtube")
                            pyttsx3.speak("Now opening "+inp+", on Youtube")
                            webbrowser.open("https://www.youtube.com/search?q=%s" % inp)

                        ni=input("Press ENTER to continue")

                    elif query == "goodbye" or query == "bye bye" or query == "exit":
                        if 19 <= currentTime.hour < 24:
                            print("Good night!",inp)
                            pyttsx3.speak("Good night!" +inp)
                            exit()
                        else:
                            print(random.choice(AR2))
                            pyttsx3.speak(random.choice(AR2))
                            exit()
                    else:
                            pyttsx3.speak("Searching on Google for "+query)
                            for url in search(query, tld="co.in", num=1, stop = 1, pause = 2):
                                webbrowser.open("https://google.com/search?q=%s" % query)
         
                except Exception as e:
                    print(e)
                    print("AURORA: ",random.choice(AR))
                    pyttsx3.speak(random.choice(AR))
                    print("Unable to Recognize your voice.")
                    pyttsx3.speak("Unable to Recognize your voice.")

        else:
            print()

    except Exception as e:
            print(e)
            print("Unable to Recognize your voice.")
            pyttsx3.speak("Unable to Recognize your voice.")
