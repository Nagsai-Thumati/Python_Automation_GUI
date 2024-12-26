from tkinter import *
from tkinter import messagebox


root = Tk()
root.title("This is Message Box Tutorial")



# Different options for Messagebox
# showinfo, showwarning, showerror, askquestion,askokcancel, askyesno
def Popup():
    response= messagebox.askyesno("Are you a Human")
    Label(root,text=response).pack()



Button(root,text="Click Here",command=Popup).pack()


mainloop()