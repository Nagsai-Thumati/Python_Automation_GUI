from tkinter import *

root = Tk()

e = Entry(root, width=50)
e.pack()


def myClick():
    hello = "Hello"+e.get()
    myLabel1= Label(root, text=hello)
    myLabel1.pack()

myButton = Button(root, text="Enter your Name", command=myClick)
myButton.pack()

root.mainloop()

