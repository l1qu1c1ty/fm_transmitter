#!/usr/bin/python

from os import path
from pydub import AudioSegment

# files
src = input("Enter MP3 file location: ")
dst = input("Enter WAV name: ")

# convert wav to mp3
sound = AudioSegment.from_mp3(src)
sound.export(dst, format="wav")