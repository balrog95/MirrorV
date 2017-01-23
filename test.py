#!/usr/bin/python

from tkinter import Tk, Frame, Label, BOTH
import time

class MirrorV(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("MirrorV")
        self.makeFullscreen()
        #make clock into its own frame and add it to the overall frame
        #possibly break clock out into its own module/class
        #maybe make it text on canvas rather than a label
        #figure out how to make it a nice looking font
        self.displayClock()
    
    def makeFullscreen(self):
        self.parent.attributes("-fullscreen", True);

    def displayClock(self):
        self.clock = Label(self.parent, font=('Helvetica', 45), bg='black')
        self.clock.pack(fill=BOTH, expand=1)
        self.time1 = ''
        self.tick()

    def tick(self):
        time2 = time.strftime('%I:%M')
        if time2 != self.time1:
            self.time1 = time2
            self.clock.config(text=time2)
        self.clock.after(2000, self.tick)

def main():
    root = Tk()
    root.geometry("250x150+300+300")
    app = MirrorV(root)
    root.mainloop()

if __name__ == '__main__':
    main()
