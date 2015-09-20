from random import randint
import os

statements = ['Great!', 'Yes.', 'No.', 'I like your ideas.']
names = ['Logan','Aspen','Pandora']

botname = names[randint(0,len(names)-1)]

def say(phrase):
    print botname + ": " + phrase
    os.system("say " + phrase)

say("Hello there!  My name is " + botname + ".")
say("What is your name? ")
name = raw_input("")
 
say("Hi " + name + "!")

while(True):
    resp = raw_input("You: ")
    
    if resp.lower() == 'what is your name?':
        say("My name is " + botname)
    elif resp.lower() == 'how far away is the sun?':
        say('92.96 million miles.')
    elif resp.lower() == 'goodbye':
        say('Goodbye! It was nice meeting you, ' + name + ".")
        exit()
    else:
        say(statements[randint(0,len(statements)-1)])
    


#ESSENTIAL CONCEPTS
# 1. Coming up with an idea
# 2. Printing strings to console
# 3. Variables and var types (ararys, etc)
# 4. Running a python script
# 5. Getting user input
# 6. Creating an infinite loop
# 7. Random integers and responses
# 8. lowercase responses
