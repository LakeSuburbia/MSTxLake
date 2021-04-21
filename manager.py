#!/usr/bin/env python

import os
import tkinter
from tkinter import *

TK_SILENCE_DEPRECATION = 1

window = Tk()
window.title("MST & Lake Suburbia maken muziek")
canvas = Canvas(window, width = 450, height = 500)

frame = Frame(window, bg="")
frame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight= 0.9)


def start():
    os.system("bash start_git.sh")
    
def stop():
    os.system("bash stop_git.sh")


startButton = Button(frame, text="START", command=start)
startButton.pack()
stopButton = Button(frame, text="STOP", command=stop)
stopButton.pack()

window.mainloop() 
