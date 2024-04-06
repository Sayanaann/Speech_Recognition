#pip install pyttsx3
import pyttsx3
txt_sp=pyttsx3.init()
text=input("enter the text..,\n")
voices=txt_sp.getProperty('voices')
for voice in voices:
    print("ID:",voice.id)
txt_sp.setProperty('voice',voices[1].id)
txt_sp.say(text)
txt_sp.runAndWait()