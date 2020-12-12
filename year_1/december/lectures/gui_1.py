from tkinter import *
import tkinter.messagebox as box
from tkinter.ttk import *

root = Tk()
root.configure(background="white")
root.title("TKinter")


def showtext(event):
    box.showinfo(text.get(1.0, END))


text = Text(width=25, height=5, wrap=WORD)
text.pack(side=LEFT)
text.bind("<Return>", showtext)


root.mainloop()
