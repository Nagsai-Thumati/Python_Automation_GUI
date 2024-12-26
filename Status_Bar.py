from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Fendt Image Viewer")


#Creating Images

Image_1 = ImageTk.PhotoImage(Image.open(r"Fendt1.png"))
Image_2 = ImageTk.PhotoImage(Image.open(r"Fendt2.png"))
Image_3 = ImageTk.PhotoImage(Image.open(r"Fendt3.png"))
Image_4 = ImageTk.PhotoImage(Image.open(r"Fendt4.png"))
Image_5 = ImageTk.PhotoImage(Image.open(r"Fendt5.png"))

Img_List = [Image_1,Image_2,Image_3,Image_4,Image_5] # List to store all the Images in it

#Label to insert Images 
My_label = Label(image=Img_List[0])
My_label.grid(row=0,column=0,columnspan=3)

#Update the Status bar
Status_Label = Label(text="Image 1 of "+str(len(Img_List)),bd=1,relief=SUNKEN,anchor=E)
Status_Label.grid(row=2,column=0,columnspan=3,sticky=W+E)



#Functions to work with Forward and Backward Buttons
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

    #Update the Status bar
    Status_Label = Label(text="Image "+str(Imag_num)+" of "+str(len(Img_List)),bd=1,relief=SUNKEN,anchor=E)
    Status_Label.grid(row=2,column=0,columnspan=3,sticky=W+E)




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

    #Update the Status bar
    Status_Label = Label(text="Image "+str(Imag_num)+" of "+str(len(Img_List)),bd=1,relief=SUNKEN,anchor=E)
    Status_Label.grid(row=2,column=0,columnspan=3,sticky=W+E)

#Creating the Buttons on root
Button_Back = Button(root,text="<<",command=back)
Button_Exit= Button(root,text="Exit",command=root.quit)
Button_Forward= Button(root,text=">>",command=lambda:forward(2))


#Inserting the buttons using grid
Button_Back.grid(row=1,column=0)
Button_Exit.grid(row=1,column=1)
Button_Forward.grid(row=1,column=2,pady=10)

root.mainloop()
