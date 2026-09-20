import ollama
from VE import V_engine
import os
chatlog = []

@staticmethod
def get_response(message):
    global chatlog
    chatlog.append(f"user: {message}")
    response = ollama.chat(
        model="gemma4",
        messages=[
            {
                "role": "user",
                "content": f"you are jarvis an ai assistant, please respond to the current prompt: {message}, chatlog {chatlog}. keep responses around 50 words max and DO NOT USE SYMBOLS IN RESPONSE",
            }
        ]
        )
    chatlog.append(f"jarvis_ai: {response.message.content}")
    V_engine.say(response.message.content)


@staticmethod
def see_image(message):
    global chatlog
    chatlog.append(f"user: (screenshot) {message}")
    response = ollama.chat(
        model="gemma4",
        messages=[
            {
                "role": "user",
                "content": f"you are jarvis an ai assistant, please respond to the image provided with the user inquiry: {message}, chatlog {chatlog}. keep responses around 50 words max and DO NOT USE SYMBOLS IN RESPONSE",
                "images": [r"temp\img.png"]
            }
        ]
        )
    os.remove(r"temp\img.png")
    chatlog.append(f"jarvis_ai: {response.message.content}")
    V_engine.say(response.message.content)

