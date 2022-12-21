# Bahaa Hamdy 20191053
# Abdelrahman Talaat 20190302

import speech_recognition as sr
import webbrowser
import time
import pyttsx3
from AppOpener import run
import wikipediaapi 
import pywhatkit
wiki_wiki = wikipediaapi.Wikipedia('en')


def record_audio(ask = False):
    with sr.Microphone(device_index=1) as source:
        if ask:
            speaking_retard(ask)
        r.energy_threshold=3000
        r.adjust_for_ambient_noise(source, 1.2)
        audio = r.listen(source)
        print("You can now speak")
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio, language="en-uk")
        except sr.UnknownValueError:
            speaking_retard('Sorry, I did not get that')
        except sr.RequestError:
            speaking_retard('sorry my speech service is down')
        return voice_data

def speaking_retard(audio_stting):
    engine.say(audio_stting)
    engine.runAndWait()

def respond(voice_data):
    if 'open calculator' in voice_data:
        run("Calculator")
        speaking_retard('opening calculator')
        return
        
    if 'play song' in voice_data:
        song = record_audio(
            'what is your song you need to play?')
        pywhatkit.playonyt(song)
        print('I play it for you brothaa')
        return
    
    if 'search' in voice_data:
        search = record_audio('Would you like to search on wikipedia or google?')
        
        if 'Wikipedia' in search:
            search = record_audio("What would you like to search for on wikipedia")
            
            wiki_page = wiki_wiki.page(search)
            if wiki_page.exists() != True:
                speaking_retard("Sorry, this page doesnt exist")
                return 
            
            for line in wiki_page.summary.split(".")[:3]:
                print(line)
                speaking_retard(line)
            return
        
        elif 'Google' in search:
            search = record_audio("What would you like to search for on google")
            url = 'https://google.com/search?q=' + search
            webbrowser.get().open(url)
            speaking_retard('here is what I found for ' + search)
            return
        return
        
        
        
    if 'kill yourself' in voice_data:
        speaking_retard('bye')
        return 0

if __name__ == "__main__":
    
    
    r = sr.Recognizer()
    engine = pyttsx3.init()
    loop_status = 1
    engine.setProperty('voice', engine.getProperty('voices')[0].id)
    time.sleep(1)
    ans = record_audio('would you like to change to a female assistant?')
    if 'yes' in ans:
        engine.setProperty('voice', engine.getProperty('voices')[1].id)
        speaking_retard("Done, what would you like me to do?")
    else:
        speaking_retard("Alright then, what would you like me to do?")
        
        
    while loop_status != 0:
        
        voice_data = record_audio()
        print(voice_data)
        loop_status = respond(voice_data)
    