#pip install SpeechRecognition
#pip install pyaudio

import speech_recognition as sr

def speech_recog():
    r=sr.Recognizer()
    mic=sr.Microphone()

    with mic as source:
        print("Speak.......")
        r.energy_threshold=500
        #r.adjust_for_ambient_noise(source,duration=1)
        audio=r.listen(source)

        try:
            text=r.recognize_google_cloud(audio)
            print("You said:",text)

        except:
            print("Didn't hear anything,pls speak again...")
speech_recog()
