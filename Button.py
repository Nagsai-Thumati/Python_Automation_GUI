from tkinter import *

root = Tk()

def myClick():
    myLabel1= Label(root, text="Look! I clicked a Button")
    myLabel1.pack()

myButton = Button(root, text="Click Me!", command=myClick, fg="blue", bg="#000000")
myButton.pack()

root.mainloop()

