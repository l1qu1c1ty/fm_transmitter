#!/usr/bin/python3

from turtle import back
from PIL import Image
from turtle import fd
from os import path
from  tkinter import *
from tkinter import filedialog
from tkinter import filedialog as fd
from gtts import gTTS
from turtle import width
from pydub import AudioSegment
import os


class Root(Tk):
    def __init__(self):
        super().__init__()

        self.title("TTS FM Radyo Oynat")
        self.geometry("350x270")
        self.resizable(width=False, height=False)
        self.configure(background="#380db8")
        
        self.img = PhotoImage(file='../images/voice.png')
        Label(self,image=self.img,bg="#380db8").place(x=120,y=10)

        self.txt1 = Entry(self)
        self.txt1.place(x=120,y=150)

        self.txt2 = Entry(self)
        self.txt2.place(x=120,y=190)

        self.lbl1 = Label(self,text="Metin Giriniz: ",bg="#380db8",fg="white")
        self.lbl1.place(x=10,y=150)
        
        self.lbl1 = Label(self,text="Frekans Giriniz: ",bg="#380db8",fg="white")
        self.lbl1.place(x=10,y=190)

        self.btn = Button(self,text="Oynat",command=self.tts,fg="white",bg="red")
        self.btn.place(x=10,y=230)

    def tts(self):
        self.txt = self.txt1.get()
        self.output = gTTS(text=self.txt,lang="tr",slow=False)
        self.output.save("../music/voice.mp3")

        src = "../music/voice.mp3"
        dst = "../music/voice.wav"
        sound = AudioSegment.from_mp3(src)
        sound.export(dst, format="wav")

        os.system("rm ../music/voice.mp3")
        os.system(f"sudo ../.././fm_transmitter ../music/voice.wav -f {self.txt2.get()} & > /dev/null")

        self.txt1.delete(0,END)

if __name__ == "__main__":
    root = Root()
    root.mainloop()