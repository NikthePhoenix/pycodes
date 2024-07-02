from tkinter import *
import tkinter.messagebox as box

myColor = '#40E0D0'

window = Tk()

window.geometry("600x700")
window.title("RPS Game")

frame = Frame(window)
def sel():
    selection = 'You selected the option ' + str(var.get())
    label.config(text = selection)

    selection= var.get()
    if selection==1:
        box.showinfo(selection)
        window.configure(bg=myColor)

var = IntVar()
R1 = Radiobutton(window, text="Cool", variable=var, value=1, )
R1.pack(pady=20)
R2 = Radiobutton(window, text="Hot", variable=var, value=2, )
R2.pack(pady=20)
R3 = Radiobutton(window, text="ice", variable=var, value=3, )
R3.pack(pady=20)

label = Label(window)
listbox=Listbox(window)
listbox.insert(1, "Rock")
listbox.insert(2, "Paper")
listbox.insert(3, "Scissor")
label.pack()

def dialog():
    try:
        user=listbox.get(listbox.curselection())
        box.showinfo('User\'s Choice',user)
    except:
        box.showerror('Error','Not Allowed')

btn=Button(window,text="vote",command=dialog)

frame.pack()
listbox.pack(padx=100,pady=150)
btn.pack(padx=300,pady=300)

window.mainloop
