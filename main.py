import speech_recognition as sr
import webbrowser
import pyttsx3
import os
import json
from langchain_huggingface import HuggingFaceEndpoint
recognizer= sr.Recognizer()
engine = pyttsx3.init()

#creating a function to impliment the command ;)
def process_command(c):
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com/")  
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com/")    
    else:
        ai_responce(c)   
        
def ai_responce(command):
    # Load HuggingFace API token from a local JSON file
    token_file_path = 'hf_token.json'

    with open(token_file_path) as f:
        data = json.load(f)
        sec_key = data['HUGGINGFACEHUB_API_TOKEN']

    # Set the environment variable for HuggingFace API token
    os.environ["HUGGINGFACEHUB_API_TOKEN"] = sec_key

    # Initialize the HuggingFace endpoint
    repo_id = "mistralai/Mistral-7B-Instruct-v0.2"
    llm = HuggingFaceEndpoint(repo_id=repo_id, max_length=128, temperature=0.7, token=sec_key)

    # Invoke the model
    command= llm.invoke(command)
    speak(command)



         
#creating a  function for speaking our desireing text :)
def speak(text):  
    voices = engine.getProperty('voices')
    
# Set the desired female voice
    for voice in voices:
        if 'zira' in voice.id.lower():  
            engine.setProperty('voice', voice.id)
            break
    engine.say(text)
    engine.runAndWait()
    

if __name__=="__main__":
    #speak("Hello mastar...i am  veronica")
    while True:
        try: 
            with sr.Microphone() as source:
                audio = recognizer.listen(source)
                
                print("recognizing....")
            text = recognizer.recognize_google(audio)   
            if(text.lower()=="veronica"):
                speak(" activating veronica...")
                speak(" yess master...")
                speak(" waiting for your commands....")
                
            with sr.Microphone() as source:
                audio = recognizer.listen(source)
                command = recognizer.recognize_google(audio)   
                process_command(command)
                
            print("You said: " + text)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
        
