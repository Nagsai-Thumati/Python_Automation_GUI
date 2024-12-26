from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

root = Tk()
root.title("This is Main GUI")


def Open():
    global my_img
    root.filename = filedialog.askopenfilename(initialdir="",title="Open the Image",filetypes=(("png files",".png"),("all files","*.*")))
    Label(root,text=root.filename).pack()
    my_img = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_img).pack()
    

Button(root,text="Open file", command=Open).pack()

mainloop()