#!/usr/bin/python3
from turtle import back
from PIL import Image
from turtle import fd
from os import path
from  tkinter import *
from tkinter import filedialog
import os

class Root(Tk):
    def __init__(self):
        super().__init__()

        os.system("setxkbmap tr")
        self.title("FM Radyo Istasyonu")
        self.geometry("350x280")
        self.resizable(width=False, height=False)
        self.configure(background="#115691")

        self.img = PhotoImage(file='../images/fm.png')
        Label(self,image=self.img,bg="#115691").place(x=120,y=10)

        self.img2 = PhotoImage(file='../images/music.png')
        Label(self,image=self.img2,bg="#115691").place(x=40,y=10)

        self.img3 = PhotoImage(file='../images/music.png')
        Label(self,image=self.img3,bg="#115691").place(x=80,y=30)

        self.img4 = PhotoImage(file='../images/music.png')
        Label(self,image=self.img4,bg="#115691").place(x=210,y=10)

        self.img5 = PhotoImage(file='../images/music.png')
        Label(self,image=self.img5,bg="#115691").place(x=250,y=30)
        
        self.lbl1 = Label(self,text="Frekans:",fg="white",bg="#115691")
        self.txt1 = Entry(self)
        self.txt2 = Entry(self,width=12,fg="darkblue")
        self.btn1 = Button(self,text="Müzik Seç",command=self.choose,fg="green")
        self.btn2 = Button(self,text="Müzik Çal",command=self.play,fg="blue")
        self.btn3 = Button(self,text="Müzik Durdur",command=self.stop,fg="red")
        self.btn4 = Button(self,text="Dönüştürme Programı",command=self.convert,fg="darkblue")
        self.btn5 = Button(self,text="Metin Mp3",command=self.tts,fg="darkblue")
        self.btn6 = Button(self,text="Metin Okuma",command=self.text2voice,fg="darkblue")
        self.btn7 = Button(self,text="Youtube Çal",command=self.ytplay,fg="darkblue")
        
        self.lbl1.place(x=10,y=130)
        self.txt2.place(x=10,y=150)
        self.btn1.place(x=10,y=180)
        self.btn2.place(x=10,y=210)
        self.btn3.place(x=10,y=240)
        self.btn4.place(x=180,y=150)
        self.btn5.place(x=180,y=180)
        self.btn6.place(x=180,y=210)
        self.btn7.place(x=180,y=240)

    def choose(self):
        self.fd = filedialog.askopenfilename(filetypes = (("wav files","*.wav"),("all files","*.*")))
        self.txt1.configure(state=NORMAL)
        self.txt1.delete(0,END)
        self.txt1.insert(0,self.fd)
        self.txt1.configure(state=DISABLED)

    def play(self):
        os.system(f"sudo ../.././fm_transmitter {self.txt1.get()} -f {self.txt2.get()} & > /dev/null")

    
    def stop(self):
        os.system(f"sudo ../.././fm_transmitter ../music/stop.wav -f {self.txt2.get()} & > /dev/null")
    
    def convert(self):
        os.system("./convert.pyw & > /dev/null")
    
    def tts(self):
        os.system("./tts.pyw & > /dev/null")

    def text2voice(self):
        os.system(f"./voice.pyw & > /dev/null")
    
    def ytplay(self):
        os.system(f"./ytplayer.pyw & > /dev/null")


if __name__ == "__main__":
    root = Root()
    root.mainloop()