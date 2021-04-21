#!/usr/bin/env python -W ignore::DeprecationWarning

import os
import tkinter
from tkinter import *

def init():
    os.system("bash init_git.sh")

def start():
    os.system("bash start_git.sh")

def stop():
    os.system("bash stop_git.sh")

root = Tk()
root.title("MST & Lake Suburbia maken muziek")
root.geometry("200x200")

initButton = Button(root, text="INIT", command=init)
initButton.pack()
startButton = Button(root, text="START", command=start)
startButton.pack()
stopButton = Button(root, text="STOP", command=stop)
stopButton.pack()

root.mainloop() 
