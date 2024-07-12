import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()  # Initialization of the recognizer once
engine = pyttsx3.init()

def process_command(c):
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com/")  
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com/")    
    elif "exit" in c.lower():  # Added an exit command
        speak("Goodbye, master.")
        exit()

def speak(text):  
    voices = engine.getProperty('voices')
    for voice in voices:  # Set the desired female voice
        if 'zira' in voice.id.lower():  
            engine.setProperty('voice', voice.id)
            break
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    while True:  # Main loop for listening and processing commands
        try:
            with sr.Microphone() as source:
                print("Listening for activation command...")
                audio = recognizer.listen(source)
                text = recognizer.recognize_google(audio)
                print(f"You said: {text}")

                if text.lower() == "veronica":  # Activation command
                    speak("Activating Veronica... Yes, master. Waiting for your commands...")

                    with sr.Microphone() as source:
                        audio = recognizer.listen(source)
                        command = recognizer.recognize_google(audio)
                        print(f"Command received: {command}")
                        process_command(command)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
