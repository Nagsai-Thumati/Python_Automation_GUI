from tkinter import *


root = Tk()
root.title("This Tutorial is to show Radio Buttons")

#Radio variable
#r= IntVar()
#r.set(2)

#Creating a list for Radio buttons
Modes = [
    ("pepperoni","pepperoni"),
    ("Cheese","Cheese"),
    ("mushrooms","mushrooms"),
    ("onions","onions")
]

#Radio Variable 
pizza = StringVar()
pizza.set("pepperoni")

for text, mode in Modes:
    Radiobutton(root,text=text,variable=pizza,value=mode).pack(anchor=W)

#Function for clicking the radio buttons
def Clicked(value):    
    Mylabel= Label(root, text=value)
    Mylabel.pack()

#Creating the radio buttons
#Radiobutton(root,text="Option 1",variable=r,value=1,command=lambda:Clicked(r.get())).pack()
#Radiobutton(root,text="Option 2",variable=r,value=2,command=lambda:Clicked(r.get())).pack()


#Label to print the options
#Mylabel= Label(root,text=pizza.get())
#Mylabel.pack()
#Button to click after selecting radio button
Button1 = Button(root,text="Click me",command=lambda:Clicked(pizza.get()))
Button1.pack()

root.mainloop()