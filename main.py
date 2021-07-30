from pytube import YouTube
from playsound import playsound
import Tkinter as tk

WIDTH = 500
HEIGHT = 150
WINDOW_TITLE = "Easy Youtube Downloader"

class YoutubeDownloader:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("()x()".format(WIDTH, HEIGHT))
        self.window.configure(bg="#d80059")
        self.window.title(WINDOW_TITLE)

        self.link_label = tk.Label(self.window, text="Download Link")
        self.name_label = tk.Label(self.window, text="Save File As")
        self.path_label = tk.Label(self.window, text="Save File Path")
        self.extension_label = tk.Label(self.window, text="File Extension")

        self.link_label.grid(column=0, row=0)
        self.name_label.grid(column=0, row=1)
        self.path_label.grid(column=0, row=2)
        self.extension_label.grid(column=0, row=3)

    def run(self):
        self.window.mainloop()
        return

if __name__ == "__main__":
    app = YoutubeDownloader()
    app.run()