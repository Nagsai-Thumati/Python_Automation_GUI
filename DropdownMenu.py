from tkinter import *

root = Tk()
root.title("This File is about Checkboxes")
root.geometry("400x400")

Days=["monday","Tuesday","Wednesday","Thursday","Friday"]

Var = StringVar()
Var.set(Days[0])

d = OptionMenu(root,Var, *Days)
d.pack()

def select():
    L = Label(root, text=Var.get()).pack()

B = Button(root, text="Click to see", command=select).pack()

mainloop()