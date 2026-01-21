
from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk
import os

app = Tk()
app.title("Welcome")
app.geometry('1550x850')

img=Image.open("demo.jpeg")
img=img.resize((1550,850))
bg=ImageTk.PhotoImage(img)
a=tk.Label(app,image=bg)
a.place(x=0,y=0)

# Add image
label = Label(app, image=bg)
label.place(x = 0,y = 0)

# Add text
label2 = Label(app, text = "ASSITIVE COMMUNICATION SYSTEM FOR DEAF,DUMB &BLIND PEOPLES",bg="#fcdf03",
               font=("Times New Roman", 24))

label2.pack(pady = 50)


def button1():
    os.system('python text_to_speech.py')
    
def button2():
    os.system('python gesture_to_voice.py')

def button3():
    os.system('python voice_to_text.py')
    
def button4():
    os.system('python image_to_voice.py')

def button5():
    os.system('python detect.py')

def button6():
    os.system('python color_detection.py')

def button7():
    os.system('python Sender.py')


def button8():
    os.system('python currency.py')


def Submit():
    pass
    
b1=tk.Button(app,text="Text to Speech",command=button1,bg="#fcdf03",activebackground="#c21d54",fg="black",font=('Arial',16),height=2,width=18)
b1.place(x=100,y=200)

b1=tk.Button(app,text="Gesture to Voice",command=button2,bg="#fcdf03",activebackground="#c21d54",fg="black",font=('Arial',16),height=2,width=18)
b1.place(x=400,y=200)

b1=tk.Button(app,text="Voice to Text",command=button3,bg="#fcdf03",activebackground="#c21d54",fg="black",font=('Arial',16),height=2,width=18)
b1.place(x=700,y=200)

b1=tk.Button(app,text="Image to Voice",command=button4,bg="#fcdf03",activebackground="#c21d54",fg="black",font=('Arial',16),height=2,width=18)
b1.place(x=1000,y=200)

b1=tk.Button(app,text="Object Detection",command=button5,bg="#fcdf03",activebackground="#c21d54",fg="black",font=('Arial',16),height=2,width=18)
b1.place(x=1300,y=200)

b1=tk.Button(app,text="Color Detection",command=button6,bg="#fcdf03",activebackground="#c21d54",fg="black",font=('Arial',16),height=2,width=18)
b1.place(x=100,y=400)


b1=tk.Button(app,text="Location",command=button7,bg="#fcdf03",activebackground="#c21d54",fg="black",font=('Arial',16),height=2,width=18)
b1.place(x=400,y=400)


b1=tk.Button(app,text="Currency Detection",command=button8,bg="#fcdf03",activebackground="#c21d54",fg="black",font=('Arial',16),height=2,width=18)
b1.place(x=700,y=400)


app.mainloop()

