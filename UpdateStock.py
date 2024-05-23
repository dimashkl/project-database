from tkinter import *
from tkinter import  ttk
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="STOCK_VEHICLE"
)

cursor = db.cursor()

def Submit():

    ID_Penjualan = combo1.get()
    Type = combo2.get()
    Product = combo3.get()
    Stock = en1.get()

    try :
        sql = "UPDATE stock_kendaraan VALUES (%s, %s, %s, %s)"
        val = ( ID_Penjualan, Type, Product, Stock)
        cursor = db.cursor()
        cursor.execute(sql,val)
        cursor.close()
        db.commit()
    except :
        print("Cannot run command, please try again!")
    else :
        print("Thank You.")
options = []
sql0 = " SELECT ID FROM stock_kendaraan"
cursor.execute(sql0)
ids = cursor.fetchall()
for i in ids:
    options.append(str(i[0]))

options1 = []
sql1 = " SELECT Type FROM stock_kendaraan"
cursor.execute(sql1)
Type = cursor.fetchall()
for i in Type:
    options1.append(str(i[0]))

options2 = []
sql2 = " SELECT Product FROM stock_kendaraan"
cursor.execute(sql2)
Product = cursor.fetchall()
for i in Product:
    options2.append(str(i[0]))

root = Tk()
global combo1
global combo2
global combo3
global en1

IDPenjualan = StringVar()
Dealer = StringVar()
Type = StringVar()
Product = StringVar()
Chassis_Number = StringVar()
Engine_Number = StringVar()
Stock = StringVar()


wrapper1 = LabelFrame(root, text="Add new stock update")
wrapper1.pack(padx=10, pady=10, fill="both")

#Label1
label1 = Label(wrapper1, text="ID Penjualan")
label1.grid(row=1, column=0, padx=10, pady=10)
combo1 = ttk.Combobox(wrapper1, textvariable=IDPenjualan)
combo1['values'] = options
combo1.grid(row=1, column=1, padx=10, pady=5)

#Label2
label2 = Label(wrapper1, text="Type")
label2.grid(row=2, column=0, padx=10, pady=10)
combo2 = ttk.Combobox(wrapper1, textvariable=Type)
combo2['values'] = options1
combo2.grid(row=2, column=1, padx=10, pady=5)

#Label3
label3 = Label(wrapper1, text="Product")
label3.grid(row=3, column=0, padx=10, pady=10)
combo3 = ttk.Combobox(wrapper1, textvariable=Product)
combo3['values'] = options2
combo3.grid(row=3, column=1, padx=10, pady=5)

#Label4
label4 = Label(wrapper1, text="Stock")
label4.grid(row=4, column=0, padx=10, pady=5)
en1 = Entry(wrapper1, textvariable=Stock)
en1.grid(row=4, column=1, padx=10, pady=5)

Button(root, text="SUBMIT", command=Submit, height= 2, width= 10).place(x=160, y=210)

cursor.close()

root.geometry("400x300")
root.title("Update")

root.mainloop()