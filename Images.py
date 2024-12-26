from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Nagasai Python Learning")
#root.iconbitmap("Nagasai")

my_image = ImageTk.PhotoImage(Image.open(r"C:\Python\GUI\Fendt1.png"))
my_label = Label(image=my_image)
my_label.pack()


Quit_button = Button(root,text="Exit Button",command=root.quit)
Quit_button.pack()

root.mainloop()