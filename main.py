#|====================|#
#|main app for program|#
#|====================|#

import customtkinter as tk
from listerner import J_listen
root = tk.CTk()

root.geometry("400x400")
root.config(bg="#2045A8")

#variables
on = False

def l_check():
    while on:
        J_listen.Listen()

def start_listen():
    global on
    if not on:
        start_listener.configure(text="Stop", fg_color="red", hover_color="red")
        on = True
    else:
        start_listener.configure(text="Start", fg_color="green", hover_color="green")
        on = False
    l_check()

start_listener = tk.CTkButton(root, text="Start", command=start_listen, fg_color="green", hover_color="green", border_width=1, border_color="black")
start_listener.place(relx=0.5, rely=0.8, anchor=tk.CENTER)
root.mainloop()