import webbrowser
import pyautogui
import win32gui
ops = {
    "browser": [webbrowser.open, "https://", None], 
    "spotify": [webbrowser.open, "https://open.spotify.com", None],
    "youtube": [webbrowser.open, "https://youtube.com", None]
    }


class commands():
    def open(message):
        m = message.split(' ', 1)[1]
        if m in ops:
            ops[m][0](ops[m][1], ops[m][2])
    def search(message):
        m = message.split(' ', 1)[1]
        webbrowser.open(f"https://{m}")
    def minimise(message):
        m = message.split(' ', 1)[1]
        windows = pyautogui.getWindowsWithTitle(m) 
        if windows:
            win = windows[0]
            win.minimize()
    def maximise(message):
        m = message.split(' ', 1)[1]
        windows = pyautogui.getWindowsWithTitle(m) 
        if windows:
            win = windows[0]
            win.maximize()
    def focus(message):
        m = message.split(' ', 1)[1]
        window = pyautogui.getWindowsWithTitle(m)
        if window.isMinimized:
            window.restore()
        window.activate() 