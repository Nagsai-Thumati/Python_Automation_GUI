from tkinter import *
from PIL import ImageTk,Image
import sqlite3

root = Tk()
root.title("Database Application")
root.geometry("400x400")

#Databases

#Create a database or connect to one
Conn = sqlite3.connect("address_book.db")

#Create a cursor
c = Conn.cursor()

#create a table
c.execute("""CREATE TABLE addresss (
          first_name text,
          last_name text,
          address text,
          city text,
          state text,
          zipcode integer
          )  """)

#Commit changes
Conn.commit()

#Close Connection
Conn.close()

mainloop()