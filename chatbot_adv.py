from random import randint
import os
import speech_recognition as sr
from chatterbot import ChatBot

names = ['Logan','Aspen','Pandora']

botname = names[randint(0,len(names)-1)]

# Create a new instance of a ChatBot
bot = ChatBot(botname, io_adapter="chatterbot.adapters.io.NoOutputAdapter")

#train the bot
conversation = [
"Hello",
"Hi there!",
"How are you doing?",
"I'm doing great.",
"That is good to hear",
"Thank you.",
"Your welcome."
]

bot.train(conversation)

def say(phrase):
    print(botname + ": " + phrase)
    os.system("say " + phrase)
    
say("Hello there!  My name is " + botname + ".")
say("What is your name? ")
name = raw_input("");
 
say("Hi " + name + "!")

#setup recognizer object
r = sr.Recognizer()

def recognizeAudio():
    with sr.Microphone() as source:
        print("You:")
        audio = r.listen(source)

    # recognize speech using Google Speech Recognition
    try:
        print(r.recognize_google(audio))
        return r.recognize_google(audio);
    except sr.UnknownValueError:
        say("Sorry I could not understand you. Please say it again");
        return None;
    except sr.RequestError:
        say("Could not request results from Google Speech Recognition service.") 
        return None;

def runBot():
    resp = recognizeAudio();
    
    if(resp != None):
        if(resp.lower() == 'goodbye'):
            say('Goodbye! It was nice meeting you, ' + name + ".")
            exit()
        
        say(bot.get_response(resp))

while(True):
    runBot();
    

#ESSENTIAL CONCEPTS
# 1. Coming up with an idea
# 2. Printing strings to console
# 3. Variables and var types (ararys, etc)
# 4. Running a python script
# 5. Getting user input
# 6. Creating an infinite loop
# 7. Random integers and responses
# 8. lowercase responses

# NEEDS PYAUDIO AND SPEECHRECOGNITION 3.0
# Chatterbot & ntlk