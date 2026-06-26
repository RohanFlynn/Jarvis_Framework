import speech_recognition as sr

rec = sr.Recognizer()


class J_listen():
    def __init__(self):
        pass
    def Listen():
        with sr.Microphone() as source:
            rec.adjust_for_ambient_noise(source)
            try:
                audio = rec.listen(source, timeout=5)
                text = rec.recognize_google(audio)
                if "jarvis" in text.lower():
                    #run command to active jarvis functions
                    print("you said jarvis")
            except sr.WaitTimeoutError:
                pass
            except sr.UnknownValueError:
                pass
            except sr.RequestError as e:
                pass
        

