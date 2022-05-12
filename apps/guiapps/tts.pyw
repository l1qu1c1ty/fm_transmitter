#!/usr/bin/python 
import os
from turtle import fd
from gtts import gTTS
from os import path
from  tkinter import *
from tkinter import filedialog

class Voice(Tk):
    def __init__(self):
        super().__init__()

        self.title("TTS")
        self.geometry("350x300")
        self.resizable(width=False, height=False)
        self.configure(background="#b8a70d")

        self.img = PhotoImage(file='../images/tts.png')
        Label(self,image=self.img,bg="#b8a70d").place(x=120,y=10)

        self.txt1 = Entry(self)
        self.txt1.place(x=5,y=150)

        self.txt2 = Entry(self)
        self.txt2.place(x=5,y=200)

        self.button1 = Button(self,text="Dosya Aç",command=self.file)
        self.button1.place(x=10,y=270)

        self.button2 = Button(self,text="Dönüştür",command=self.tts)
        self.button2.place(x=90,y=270)

        self.label1 = Label(self,text="Dosya Konumu (txt):",bg="#b8a70d",fg="white")
        self.label1.place(x=2,y=130)

        self.label2 = Label(self,text="Dosya Konumu (mp3):",bg="#b8a70d",fg="white")
        self.label2.place(x=2,y=180)

    def file(self):
        self.fd = filedialog.askopenfilename(filetypes = (("text files","*.txt"),("all files","*.*")))
        self.txt1.delete(0,END)
        self.txt1.insert(0,self.fd)


    def tts(self):
        self.file = open(self.txt1.get(),encoding="utf-8")
        self.txt = self.file.read()
        self.output = gTTS(text=self.txt,lang="tr",slow=False)
        self.output.save(self.txt2.get())
        self.file.close()


if __name__ == "__main__":
    root = Voice()
    root.mainloop()