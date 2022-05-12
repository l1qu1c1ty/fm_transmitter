#!/usr/bin/python3
from __future__ import unicode_literals
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
import youtube_dl
import os


class Root(Tk):
    def __init__(self):
        super().__init__()

        self.title("Youtube FM Radyo Oynat")
        self.geometry("350x260")
        self.resizable(width=False, height=False)
        self.configure(background="#7700ff")


        self.img = PhotoImage(file='../images/yt.png')
        Label(self,image=self.img,bg="#7700ff").place(x=120,y=10)


        self.txt1 = Entry(self,fg="#7700ff")
        self.txt2 = Entry(self,fg="#7700ff")
        self.lbl1 = Label(self,text="Youtube Link: ",bg="#7700ff",fg="white")
        self.lbl2 = Label(self,text="Frekans Giriniz: ",bg="#7700ff",fg="white")
        self.btn = Button(self,text="Oynat",command=self.Play,fg="white",bg="red")
        
        self.txt1.place(x=120,y=150)
        self.txt2.place(x=120,y=190)
        self.lbl1.place(x=10,y=150)
        self.lbl2.place(x=10,y=190)
        self.btn.place(x=10,y=230)


    def Play(self):
        os.system("rm ../music/ytmusic.mp3")
        self.ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
        }],
        'outtmpl': '../music/ytmusic.%(ext)s'
        } 
        with youtube_dl.YoutubeDL(self.ydl_opts) as ydl:
            ydl.download([self.txt1.get()])
        
        src = "../music/ytmusic.mp3"
        dst = "../music/ytmusic.wav"
        sound = AudioSegment.from_mp3(src)
        sound.export(dst, format="wav")
        
        os.system(f"sudo ../.././fm_transmitter ../music/ytmusic.wav -f {self.txt2.get()} & > /dev/null")
        self.txt1.delete(0,END)

if __name__ == "__main__":
    root = Root()
    root.mainloop()