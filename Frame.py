from tkinter import *

root = Tk()
root.title("This is example to show Frame")


#Creating a frame
My_Frame = LabelFrame(root,text="This is a Frame",padx=50,pady=50)
My_Frame.pack(padx=20,pady=20)

#Creating a button inside Frame
Button1= Button(My_Frame,text='Click here and it does nothing')
Button2 = Button(My_Frame,text="Even this do nothin")
Button1.grid(row=0,column=0)
Button2.grid(row=1,column=0)

root.mainloop()