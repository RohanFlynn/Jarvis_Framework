#|====================|#
#|main app for program|#
#|====================|#

import customtkinter as tk
root = tk.CTk()

root.geometry("400x400")
root.config(bg="#2045A8")

def start_listen():
    pass

start_listener = tk.CTkButton(root, text="Start", command=start_listen)
start_listener.place(x=140, y=250)
root.mainloop()