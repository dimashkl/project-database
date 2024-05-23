import tkinter as tk
from tkinter import *
from tkinter import ttk
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="STOCK_VEHICLE"
)

cursor = db.cursor()

sql = "SELECT * from m_type"
cursor.execute(sql)
rows = cursor.fetchall()

root = Tk()

Frm = Frame(root)
Frm.pack(side=tk.LEFT, padx=20)

tree = ttk.Treeview(Frm, columns=(1,2,3), show="headings", height="5")
tree.pack()

tree.heading(1, text="Name")
tree.heading(2, text="Age")
tree.heading(3, text="Email")

for i in rows:
    tree.insert('', 'end', values=i)

root.title("Master Table of Type")
root.geometry("650x500")
root.mainloop()