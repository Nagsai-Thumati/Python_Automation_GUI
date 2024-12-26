from tkinter import *

root = Tk()
root.title("This File is about Checkboxes")
root.geometry("400x400")

Var = IntVar()


C = Checkbutton(root, text="Select to get Onions as topping", variable= Var)
C.pack()

def select():
    L = Label(root, text=Var.get()).pack()

B = Button(root, text="Click to see", command=select).pack()

mainloop()