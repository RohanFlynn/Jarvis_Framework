#|====================|#
#|main app for program|#
#|====================|#

import customtkinter as tk
from listerner import Listen, mode
import threading

root = tk.CTk()
root.iconbitmap(r"static\icon.ico")
root.geometry("400x400")
root.config(bg="#2045A8")

#variables
on = False
listener_thread = None
ai = False
def l_check():
    while on:
        Listen()

def start_listen():
    global on
    if not on:
        start_listener.configure(text="Stop", fg_color="red", hover_color="red")
        on = True
        listener_thread = threading.Thread(target=l_check, daemon=True)
        listener_thread.start()
    else:
        start_listener.configure(text="Start", fg_color="green", hover_color="green")
        on = False

def swap_modes():
    global ai
    if not ai:
        ai_mode_button.configure(text="ai mode")
        ai = True
    else:
        ai_mode_button.configure(text="command mode")
        ai = False
    mode(ai)

start_listener = tk.CTkButton(root, text="Start", command=start_listen, fg_color="green", hover_color="green", border_width=1, border_color="black")
start_listener.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

ai_mode_button = tk.CTkButton(root, text="command mode", fg_color="blue", hover_color="purple", border_width=1, border_color="black", command=swap_modes)
ai_mode_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)
root.mainloop()