import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser

engine = pyttsx3.init()

def sayToMe(talk):
    engine.say(talk)
    engine.runAndWait()

sayToMe("Hello everyone, everything is worked")
sayToMe("Say something")
# for index, name in enumerate(sr.Microphone.list_microphone_names()):
#      print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

record = sr.Recognizer()
try:
    with sr.Microphone(device_index=0) as source:
        print("Say...")
        audio = record.listen(source)
        result = record.recognize_google(audio)
        result = result.lower
        print(result)

        if result == 'Say me time':
            now = datetime.datetime.now()
            str_date = "Now {}:{}".format(str(now.hour), str(now.minute))
            print(str_date)
            sayToMe(str_date)
        elif result == "Open web-browser":
            webbrowser.open("https://itproger.com")


except sr.UnknownValueError:
    print("The voice was not recognized")
except sr.RequestError:
    print("Something went wrong...")


