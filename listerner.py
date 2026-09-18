import speech_recognition as sr
import pyttsx3
from commands import commands
from jarvis import get_response
rec = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) 

ai = False

@staticmethod
def Listen():
    with sr.Microphone() as source:
        rec.adjust_for_ambient_noise(source)
        try:
            audio = rec.listen(source, timeout=5)
            text = rec.recognize_google(audio)
            if "jarvis" in text.lower():
                #run command to active jarvis functions
                engine.say("Yes?")
                engine.runAndWait()
                with sr.Microphone() as source:
                    try:
                        audio2 = rec.listen(source, timeout=10, phrase_time_limit=10)
                        text2 = str(rec.recognize_google(audio2)).lower()
                        print(text2)
                        if not ai:
                            try:
                                func = getattr(commands, text2.split()[0])
                                func(text2)
                            except AttributeError:
                                pass
                        else:
                            get_response(text2)
                    except sr.WaitTimeoutError:
                        pass
                    except sr.UnknownValueError:
                        pass
                    except sr.RequestError as e:
                        pass
        except sr.WaitTimeoutError:
            pass
        except sr.UnknownValueError:
            pass
        except sr.RequestError as e:
            pass


@staticmethod
def mode(mod):
    global ai
    ai = mod
        

