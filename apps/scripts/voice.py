#!/bin/python

from gtts import gTTS
import os
from os import path

file = open("/home/melih/fm_transmitter/scripts/voice.txt",encoding="utf-8")
txt = file.read()
output = gTTS(text=txt,lang="tr",slow=False)
output.save("voice.mp3")
file.close()
