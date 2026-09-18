import ollama
import pyttsx3


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) 


chatlog = []

@staticmethod
def get_response(message):
    global chatlog
    chatlog.append(f"user: {message}")
    response = ollama.chat(
        model="gpt-oss:20b-cloud",
        messages=[
            {
                "role": "user",
                "content": f"you are jarvis an ai assistant, please respond to the current prompt: {message}, chatlog {chatlog}. keep responses around 50 words max and DO NOT USE SYMBOLS IN RESPONSE",
            }
        ]
        )
    chatlog.append(f"jarvis_ai: {response.message.content}")
    engine.say(response.message.content)
    engine.runAndWait()