from tkinter import *
import tkinter.messagebox as box

window = Tk()

window.geometry("700x500")

window.title("Greeting")

instruction_label = Label(window, text="Input your name: ")
instruction_label.pack(pady=20)

mystring_Friend1 = StringVar()
mystring_Friend2 = StringVar()

name_entry = Entry(window, textvariable=mystring_Friend1)
name_entry.pack(pady=20)

def display_name():
    msg = "BE CALM! \n" + mystring_Friend1.get()
    box.showerror("Welcome", msg)

#create a button to submit the name
submit_button = Button(window, text="Submit", command=display_name)
submit_button.pack(pady=20)

window.mainloop