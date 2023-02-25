import speech_recognition as sr
import pyttsx3
listener=sr.Recognizer() 
import pywhatkit
import datetime
import wikipedia
import pyjokes
# // to recognize our words

# for robo to talk to me

engine=pyttsx3.init()
#to make the voice of female

voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def talk(text):

    engine.say(text)
    engine.runAndWait()

def take_command():
    try:

        with sr.Microphone() as source:

            print('Listening....')
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            if 'robo' in command:
                command=command.replace('robo','')
                print(command)
    except:

        pass

    return command

def run_robo():
    command=take_command()
    print(command)
    if 'play' in command:
        song=command.replace('play','')
        talk('playing'+song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time=datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('current time is '+time)
    elif 'who is' in command:
        person=command.replace('who is','')
        info=wikipedia.summary(person,1) #only first line
        talk(info)
    elif 'what is' in command:
        object=command.replace('what is','')
        inf=wikipedia.summary(object,1)
        talk(inf)    
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('please tell again') 
run_robo()        