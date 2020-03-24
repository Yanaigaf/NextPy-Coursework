'''
find a module that can read out text and have it read out "first time i'm using a package in next.py course"

module installed - pyttsx3 version 2.71(!) latest pyttsx3 version does not support my local python version
'''

import pyttsx3
engine = pyttsx3.init()
engine.say("first time i'm using a package in next.py course")
engine.runAndWait()
