#!/usr/bin/python3
from tkinter import *
from tkinter import filedialog as fd
from turtle import width
from pydub import AudioSegment

def ChooseFile():
    filetypes = (
        ('MP3 Files', '*.mp3'),
        ('All Files', '*.*'))

    filename = fd.askopenfilename(
        title='Open',
        initialdir='/home/pi',
        filetypes=filetypes)

    txt1.insert(0,filename)

def Convert():
    src = txt1.get()
    dst = txt2.get()
    sound = AudioSegment.from_mp3(src)
    sound.export(dst, format="wav")

root = Tk()
root.title("MP3 WAV Donusturme")
root.geometry("320x280")
root.resizable(width=False, height=False)
root.configure(background="#14b84b")

img = PhotoImage(file='../images/wav.png')
Label(root,image=img,bg="#14b84b").place(x=100,y=10)

lbl1 = Label(root,text="MP3 Dosya Konumu:",bg="#14b84b",fg="white")
lbl2 = Label(root,text="WAV Dosya Konumu:",bg="#14b84b",fg="white")
txt1 = Entry(root,width=42)
txt2 = Entry(root,width=42)
btn1 = Button(root,text = "Dönüştür",command=Convert)
btn2 = Button(root,text = "Dosya Seç",command=ChooseFile)

btn1.place(x=10,y=250) 
btn2.place(x=100,y=250)

txt1.place(x=10,y=130)
txt2.place(x=10,y=200)

lbl1.place(x=10,y=110)
lbl2.place(x=10,y=180)

root.mainloop()