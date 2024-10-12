import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os
import webbrowser
import pywhatkit as kit
import pyjokes
import requests
import instaloader
import pyautogui 
import PyPDF2

engine = pyttsx3.init()
voice= engine.getProperty('voices')
engine.setProperty('voice',voice[0].id)
engine.setProperty('rate',180)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)
    
def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)
    
def greeting():
    hour = datetime.datetime.now().hour
    if hour >= 4 and hour <= 11:
        speak("Good Morning")
    elif hour >= 12 and hour <=16:
        speak("Good afternoon")
    elif hour >= 17 and hour <= 20:
        speak("Good evening")
    # else:
        # speak("Good Night")
    speak("I'm your AI assistant, please tell me how can i help you")
    
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source: 
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again please...")
        
        return "None"
    return query

def pdf_reader():
    b = input("Enter book name here: ")
    book = open(b+'.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    speak(f"Total number of pages in this book: {pages}")
    speak("Sir, please enter the page number I have to read:")
    pg = int(input("Please enter the page number: "))  # You can replace this with a call to takecommand() if you have such a function
    if pg < 0 or pg > pages:
        speak("Invalid page number.")
        return
    page = pdfReader.getPage(pg)
    text = page.extractText()
    speak(text)

if __name__ == "__main__":
    greeting()
    while True:
        query = takecommand().lower()
        
        if 'time' in query:
            time()
        
        elif 'date' in query:
            date()
            
        elif 'how are you' in query:
            speak("I am doing well, thank you for asking!")

        elif 'had your breakfast' in query:
            speak("I don't eat food, but thank you for asking!")

        elif 'good morning' in query:
            speak("Good morning! How can I assist you today?")

        elif 'good afternoon' in query:
            speak("Good afternoon! How may I help you?")

        elif 'good evening' in query:
            speak("Good evening! Is there anything I can assist you with?")

        elif 'good night' in query:
            speak("Good night! Sweet dreams.")
            quit()
            
        elif 'bye' in query or 'exit' in query:
            speak("Goodbye! Have a great day!")
            quit()
            
        elif 'how old are you' in query:
            speak("I am an AI assistant, so I don't age like humans.")

        elif 'who created you' in query:
            
            speak(f"I was created by Priyanka")

            
        elif 'what is' in query:
            speak("Searching...")
            query = query.replace("what is", "").strip()  # Remove "what is" and any leading/trailing whitespace
            try:
                result = wikipedia.summary(query, sentences=3)
                print(result)
                speak(result)
            except wikipedia.exceptions.DisambiguationError as e:
                options = e.options[:3]  # Limiting to the first 3 options for simplicity
                speak(f"There are multiple options for {query}. Here are some: {', '.join(options)}")
            except wikipedia.exceptions.PageError:
                speak(f"Sorry, I couldn't find any information about {query}.")
            except Exception as e:
                print(e)
                speak("Sorry, I encountered an error while processing your request.")

            
        elif 'who is' in query:
            speak("Searching...")
            query = query.replace("who is", "").strip()  # Remove "what is" and any leading/trailing whitespace
            try:
                result = wikipedia.summary(query, sentences=3)
                print(result)
                speak(result)
            except wikipedia.exceptions.DisambiguationError as e:
                options = e.options[:3]  # Limiting to the first 3 options for simplicity
                speak(f"There are multiple options for {query}. Here are some: {', '.join(options)}")
            except wikipedia.exceptions.PageError:
                speak(f"Sorry, I couldn't find any information about {query}.")
            except Exception as e:
                print(e)
                speak("Sorry, I encountered an error while processing your request.")
        
        elif 'offline' in query:
            speak("going offline...")
            hour = datetime.datetime.now().hour
            if hour >=21 and hour <=3 :
                speak("Good night")
            quit()
            
        elif 'open notepad' in query:
            path = "C:\\Windows\\notepad.exe"
            speak("opening notepad")
            os.startfile(path)
            
        elif 'open google' in query:
            webbrowser.open('http://www.google.com')
            
            
        elif 'open command prompt' in query:
            os.system("start cmd")
            
        elif 'open youtube' in query:
            webbrowser.open('http://www.youtube.com')
        
        elif 'open facebook' in query:
            webbrowser.open('http://www.facebook.com')
        
        elif 'search in google' in query:
            speak("I'll help you search in google, please tell me what should I search")
            search = takecommand().lower()
            webbrowser.open(f"{search}")
            result = wikipedia.summary(search,sentences=2)
            speak(result)
            
        elif 'send message' in query:
            speak("Please provide the number to send the message.")
            num = takecommand().lower()
            num = num.replace(" ", "")
            num = num.replace("-", "")
            
            if num.isdigit():
                phnum = "+91" + num 
                print("Phone number:", phnum) 
                speak("Please confirm if this phone number is correct. Say yes or no.")
                res = takecommand().lower()
                
                if 'yes' in res:
                    speak("What message would you like to send?")
                    content = takecommand()
                    
                    try:
                        hr = int(datetime.datetime.now().strftime("%H"))
                        min = int(datetime.datetime.now().strftime("%M"))
                        smin = min + 1
                        kit.sendwhatmsg(phnum, content, hr, smin)
                        
                    except Exception as e:
                        print("Error:", e)
                        speak("Sorry, there was an error sending the message. Please try again.")
                else:
                    speak("Sorry, please try again with the correct phone number.")
            else:
                speak("Invalid phone number. Please provide a valid phone number.")

        elif 'play video' in query:
            speak("which video should i play?")
            song = takecommand().lower()
            kit.playonyt(song)
            
        elif 'play song' in query:
            speak("which song should i play?")
            song = takecommand().lower()
            kit.playonyt(song)
            
        elif 'close notepad' in query:
            speak("closing notepad")
            os.system("taskkill /f /im notepad.exe")
            
        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)
            
        elif "shut down the system" in query:
            os.system("shutdown /s /t 1")
            
        elif "restart the system" in query:
            os.system("shutdown /r /t 1")
            
        elif "logout" in query:
            os.system("shutdown -l")
            
        elif 'close browser' in query:
            os.system("taskkill /f /im msedge.exe")
            
        elif 'close chrome' in query:
            os.system("taskkill /f /im chrome.exe")
            
        elif "switch window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            pyautogui.keyUp("alt")
            
        elif "where i am" in query:
            speak("wait sir , let me check")
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                print(ipAdd)
                url = 'https://get.geojs.io/v1/ip/geo/' + ipAdd + '.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                #print(geo_data)
                city = geo_data['city']
                state = geo_data['region']
                country = geo_data['country']
                speak(f"Sir, I am not sure, but I think we are in {city} city of {state} state of {country} country.")
            except Exception as e:
                speak("Sorry sir, due to a network issue, I am not able to find where we are.")
                pass
            
        elif "instagram profile" in query or "profile on instagram" in query:
            speak("Sir, please enter the username correctly.")
            name = input("Enter username here: ")
            webbrowser.open(f"https://www.instagram.com/{name}")
            speak(f"Sir, here is the profile of the user {name}.")
            #time.sleep(5)
            speak("Sir, would you like to download the profile picture of this account?")
            condition = takecommand().lower()
            if "yes" in condition:
                mod = instaloader.Instaloader()
                mod.download_profile(name, profile_pic_only=True)
                speak("Sir, I am done. The profile picture is saved in our main folder. Now I am ready.")
            else:
                pass
            
        elif "take screenshot" in query or "take a screenshot" in query:
            speak("Sir, please tell me the name for this screenshot file.")
            name = takecommand().lower()  
            speak("Please sir, hold the screen for a few seconds, I am taking a screenshot.")
            #time.sleep(3)  
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("I am done sir, the screenshot is saved in our main folder. Now I am ready.")
        
        elif "read pdf" in query:
            pdf_reader()
            
        elif "thank you" in query:
            speak("its my pleasure")
            
        elif "hide all files" in query or "hide this folder" in query or "visible for everyone" in query:
            speak("Sir, please tell me if you want to hide this folder or make it visible for everyone.")
            condition = takecommand().lower()
            if "hide" in condition:
                os.system("attrib +h /s /d") 
                speak("Sir, all the files in this folder are now hidden.")
            elif "visible" in condition:
                os.system("attrib -h /s /d") 
                speak("Sir, all the files in this folder are now visible to everyone.")
            elif "leave it" in condition or "leave for now" in condition:
                speak("Ok sir")
        
        # speak("Do you have any other work")
            
            