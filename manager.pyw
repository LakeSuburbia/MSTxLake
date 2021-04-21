#!/usr/bin/env python -W ignore::DeprecationWarning

import os
import tkinter
from tkinter import *

TK_SILENCE_DEPRECATION=1
PYTHONWARNINGS="ignore::DeprecationWarning:simplejson"

def init():
    os.system("bash init_git.sh")

def start():
    os.system("bash start_git.sh")

def stop():
    os.system("bash stop_git.sh")

root = Tk()
root.title("Daan's supercoole writetracker")
root.geometry("400x400")

initButton = Button(root, text="INIT", command=init)
initButton.pack()
startButton = Button(root, text="START", command=start)
startButton.pack()
stopButton = Button(root, text="STOP", command=stop)
stopButton.pack()

root.mainloop() 
