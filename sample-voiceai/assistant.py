import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os
import sys

# Initialize speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 170)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Female voice

def talk(text):
    print("PRIYA:", text)
    engine.say(text)
    engine.runAndWait()

def take_command():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        listener.adjust_for_ambient_noise(source)
        voice = listener.listen(source)
    try:
        command = listener.recognize_google(voice)
        command = command.lower()
        print("You said:", command)
    except sr.UnknownValueError:
        talk("Sorry, I didn’t catch that.")
        return ""
    except sr.RequestError:
        talk("Network issue with Google service.")
        return ""
    return command

def run_priya():
    command = take_command()

    if "play" in command:
        song = command.replace("play", "").strip()
        talk("Playing on YouTube")
        pywhatkit.playonyt(song)

    elif "what's the time" in command or "what is the time" in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk(f"The time is {time}")

    elif "who is my master" in command or "who is your master" in command:
        talk("You are my master, Boss")

    elif "who is" in command:
        person = command.replace("who is", "").strip()
        try:
            info = wikipedia.summary(person, sentences=1)
            talk(info)
        except:
            talk("Sorry, I couldn’t find information about that person.")

    elif "joke" in command:
        talk(pyjokes.get_joke())

    elif "open chrome" in command:
        chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        if os.path.exists(chrome_path):
            talk("Opening Chrome")
            os.startfile(chrome_path)
        else:
            talk("Chrome path not found")

    elif "open code" in command or "open vs code" in command:
        talk("Opening Visual Studio Code")
        os.system("code")

    elif "exit" in command or "stop" in command:
        talk("Goodbye Boss")
        sys.exit()

    elif command != "":
        talk("I heard you, but I don’t understand that yet")

talk("Hello Boss. I am PRIYA, your personal voice assistant.")
while True:
    run_priya()
