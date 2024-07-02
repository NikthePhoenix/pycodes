from tkinter import *
import random
import tkinter.messagebox as box

window=Tk()
window.title("RPS Game")

frame = Frame(window)

listbox=Listbox(frame)
listbox.insert(1,"Rock")
listbox.insert(2,"Paper")
listbox.insert(3, "Scissor")

var = IntVar()
R1 = Radiobutton(window, text="Option 1", variable=var, value=1, )
R1.pack(anchor = W)
# R2 = Radiobutton(window, text="Option 2", variable=var, value=2, )


def dialog():
    user=listbox.get(listbox.curselection())
    
    box.showinfo('Users\'s Choice', user)

btn=Button(frame, text="vote", command=dialog)


frame.pack(padx=200,pady=200)
listbox.pack(padx=100,pady=50)
btn.pack(padx=50, pady=50)
