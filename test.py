#!/usr/bin/python

from tkinter import Tk, Frame, Label, BOTH
import time

class Display(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")
        self.parent = parent
        self.time1 = ''
        self.initUI()

    def initUI(self):
        self.parent.title("MirrorV")
        self.pack(fill=BOTH, expand=1)
        self.makeFullscreen()
        self.displayClock()
    
    def makeFullscreen(self):
        self.parent.attributes("-fullscreen", True);

    def displayClock(self):
        self.clock = Label(self.parent, font=('times', 20, 'bold'), bg='green')
        self.clock.pack(fill=BOTH, expand=1)
        self.tick()

    def tick(self):
        time2 = time.strftime('%H:%M:%S')
        if time2 != self.time1:
            self.time1 = time2
            self.clock.config(text=time2)
        self.clock.after(200, self.tick)

def main():
    root = Tk()
    root.geometry("250x150+300+300")
    app = Display(root)
    root.mainloop()

if __name__ == '__main__':
    main()
