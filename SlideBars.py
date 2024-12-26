from tkinter import *

root = Tk()
root.title("This File is about Slide Bars")
root.geometry("400x400")

Vertical = Scale(root,from_=0,to=400)
Vertical.pack()


def Click():
    root.geometry(str(Horizontal.get())+"x"+str(Vertical.get()))


Horizontal = Scale(root, from_=0, to=400, orient=HORIZONTAL)
Horizontal.pack()

My_Btn = Button(root, text="Click to change GUI Size",command= Click).pack()




mainloop()