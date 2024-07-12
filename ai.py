import speech_recognition as sr
import webbrowser
import pyttsx3
import os
import json
from langchain_huggingface import HuggingFaceEndpoint
recognizer= sr.Recognizer()
engine = pyttsx3.init()


def speak(text):  
    voices = engine.getProperty('voices')
    
# Set the desired female voice
    for voice in voices:
        if 'zira' in voice.id.lower():  
            engine.setProperty('voice', voice.id)
            break
    engine.say(text)
    engine.runAndWait()
    






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
response = llm.invoke("What is machine learning")
speak(response)
