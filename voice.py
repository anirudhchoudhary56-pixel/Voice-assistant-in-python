import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize the voice engine
engine = pyttsx3.init()
engine.setProperty('rate', 170)  # Speed of speech
engine.setProperty('volume', 1.0)  # Volume (0.0 to 1.0)

def speak(text):
    """Convert text to speech"""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen to the user's voice and return as text"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio, language='en-in')
        print(f"You said: {command}\n")
    except Exception as e:
        print("Sorry, could not understand. Please say that again.")
        return ""
    return command.lower()

def wish_user():
    """Wish the user based on time"""
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am your voice assistant. How can I help you today?")

def run_assistant():
    wish_user()
    while True:
        command = listen()

        if 'time' in command:
            time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {time}")

        elif 'date' in command:
            date = datetime.datetime.now().strftime("%B %d, %Y")
            speak(f"Today's date is {date}")

        elif 'open google' in command:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")

        elif 'open youtube' in command:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")

        elif 'search' in command:
            speak("What do you want to search for?")
            query = listen()
            webbrowser.open(f"https://www.google.com/search?q={query}")
            speak(f"Here are the results for {query}")

        elif 'stop' in command or 'exit' in command or 'bye' in command:
            speak("Goodbye! Have a nice day!")
            break

        elif command == "":
            continue

        else:
            speak("Sorry, I don't understand that command.")

# Run the assistant
run_assistant()
