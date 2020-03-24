import sys
import base64
from tkinter import *


message = 'CgkJICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAuLS0tW1tfX11dLS0tLS4KICAgICAgICAgICAgICA7LS0tLS0tLS0tLS0tLS58ICAgICAgIF9fX18KICAgICAgICAgICAgICB8ICAgICAgICAgICAgIHx8ICAgLi0tW1tfX11dLS0tLgogICAgICAgICAgICAgIHwgICAgICAgICAgICAgfHwgIDstLS0tLS0tLS0tLS58CiAgICAgICAgICAgICAgfCAgICAgICAgICAgICB8fCAgfCAgICAgICAgICAgfHwKICAgICAgICAgICAgICB8X19fX19fX19fX19fX3wvICB8ICAgICAgICAgICB8fAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHxfX19fX19fX19fX3wvCgo='
print(base64.b64decode(message))


class App:
    def __init__(self, master):

        self.frame = Frame(master)
        self.frame.pack()

        # self.button = Button(frame, text="QUIT", fg="red", command=frame.quit)
        # self.button.pack(side=LEFT)
        self.question = Label(self.frame, text="What's my favorite video?")
        self.question.pack()

        self.hi_there = Button(
            self.frame, text="Click to find out!", command=self.show_image)
        self.hi_there.pack()

    def show_image(self):
        vidimage = PhotoImage(file='nextpy6.1image.gif')
        self.image = Label(image=vidimage)
        self.image.photo = vidimage
        self.image.pack()
        self.hi_there.destroy()


root = Tk()

app = App(root)
root.mainloop()
