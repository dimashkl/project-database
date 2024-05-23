from tkinter import *
from tkinter import messagebox
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="STOCK_VEHICLE"
)

cursor = db.cursor()



#login form
def Login():
    username = e1.get()
    password = e2.get()

    if(username == "Admin" and password == "admin") :
        messagebox.showinfo("", "Login Success!")
    elif(username == "" and password == "") :
        messagebox.showinfo("", "User Not Allowed.")
    else :
        messagebox.showinfo("", "Incorrect Username and Password.")

root = Tk()
root.title('Login Portal')
root.geometry("300x200")
global e1
global e2

Label(root, text="Username").place(x=10, y=10)
Label(root, text="Password").place(x=10, y=40)

e1 = Entry(root)
e1.place(x=140, y=10)

e2 = Entry(root)
e2.place(x=140, y=40)
e2.config(show="*")

Button(root, text="Login", command=Login, height= 2, width= 10).place(x=110, y=110)

root.mainloop()
