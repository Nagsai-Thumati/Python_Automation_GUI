from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Fendt Image Viewer")

Image_1 = ImageTk.PhotoImage(Image.open(r"Fendt1.png"))
Image_2 = ImageTk.PhotoImage(Image.open(r"Fendt2.png"))
Image_3 = ImageTk.PhotoImage(Image.open(r"Fendt3.png"))
Image_4 = ImageTk.PhotoImage(Image.open(r"Fendt4.png"))
Image_5 = ImageTk.PhotoImage(Image.open(r"Fendt5.png"))
Img_List = [Image_1,Image_2,Image_3,Image_4,Image_5]

My_label = Label(image=Img_List[0])
My_label.grid(row=0,column=0,columnspan=3)


def forward(Imag_num):
    global forward
    global My_label
    global back

    My_label.grid_forget()
    My_label = Label(image=Img_List[Imag_num-1])
    Button_Forward = Button(root, text=">>",command= lambda:forward(Imag_num+1))
    Button_Back = Button(root,text="<<",command= lambda:back(Imag_num-1))
    if Imag_num==5:
        Button_Forward=Button(root,text=">>", state=DISABLED)
    My_label.grid(row=0,column=0,columnspan=3)
    Button_Forward.grid(row=1,column=2)
    Button_Back.grid(row=1,column=0)


def back(Imag_num):
    global My_label
    global Button_Forward
    global Button_Back

    My_label.grid_forget()
    My_label = Label(image=Img_List[Imag_num-1])
    Button_Forward = Button(root, text=">>",command= lambda:forward(Imag_num+1))
    Button_Back = Button(root,text="<<",command= lambda:back(Imag_num-1))
    if Imag_num==1:
        Button_Back=Button(root,text="<<", state=DISABLED)
    My_label.grid(row=0,column=0,columnspan=3)
    Button_Forward.grid(row=1,column=2)
    Button_Back.grid(row=1,column=0)

Button_Back = Button(root,text="<<",command=back)
Button_Exit= Button(root,text="Exit",command=root.quit)
Button_Forward= Button(root,text=">>",command=lambda:forward(2))

Button_Back.grid(row=1,column=0)
Button_Exit.grid(row=1,column=1)
Button_Forward.grid(row=1,column=2)

root.mainloop()
