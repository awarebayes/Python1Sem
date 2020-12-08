from tkinter import *
import tkinter.messagebox as box
from tkinter.ttk import *

root = Tk()
root.configure(background="white")

w = Label(root, text="Enter your name and click toggle!")
w.pack(side=LEFT)

btn_end = Button(root, text="Exit")
btn_end.pack(side=RIGHT)
btn_end.bind('<Button-1>', exit)

name_text = Entry(root)
name_text.pack(side=LEFT)

def toggle():
    w.configure(text=f"Hello {name_text.get()}")

btn_toggle = Button(root, text="toggle", command=toggle)
btn_toggle.pack(side=LEFT)


root.mainloop()
