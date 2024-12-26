from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("This is Main GUI")


def ImageGUI():
    global my_img
    top = Toplevel()
    top.title("This is Image GUI")
    my_img= ImageTk.PhotoImage(Image.open("Fendt2.png"))
    Label(top, image=my_img).pack()
    Button(top,text="Click to close",command=top.destroy).pack()



Button(root,text="Click to open Image", command=ImageGUI).pack()

root.mainloop()