from tkinter import *
window=Tk()
window.geometry("500x500")
window.title("Buttons")
def hello():
    print("hello sir")
def name():
    print("what is your name")
def age():
    print("what is your age")
def color():
    print("tell your favourite color")


b1=Button(window,text="PRESS ME",bg="black",font=("ariel",15,"bold"),fg="white",borderwidth=12,relief=SUNKEN,command=hello)
b2=Button(window,text="PRESS ME",bg="black",font=("ariel",15,"bold"),fg="white",borderwidth=12,relief=SUNKEN,command=name)
b3=Button(window,text="PRESS ME",bg="black",font=("ariel",15,"bold"),fg="white",borderwidth=12,relief=SUNKEN,command=age)
b4=Button(window,text="PRESS ME",bg="black",font=("ariel",15,"bold"),fg="white",borderwidth=12,relief=SUNKEN,command=color)
b1.pack(side="left",anchor="n",padx="30")
b2.pack(side="left",anchor="n",padx="30")
b3.pack(side="left",anchor="n",padx="30")
b4.pack(side="left",anchor="n",padx="30")
window.mainloop()