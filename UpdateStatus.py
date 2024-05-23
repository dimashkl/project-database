from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="STOCK_VEHICLE"
)

cursor = db.cursor()
#Update Data Form

# List of colors
TZ40_colors = [
    "Kuning"
]

TW50_colors = [
    "Kuning"
]

TV50_colors = [
    "Merah Pertamina",
    "Kuning"
]

TR50_colors = [
    "Kuning"
]

TQ40_colors = [
    "Abu-Abu"
]

TM50_colors = [
    "Hitam"
]

TL50_colors = [
    "Kuning"
]

TK50_colors = [
    "Kuning"
]

TI40_colors = [
    "Hitam"
]

TH40_colors = [
    "Kuning"
]

TG40_colors = [
    "Kuning"
]

PT20_colors = [
    "Oranye"
]

def Submit():

    Dealer = combo1.get()
    Type = combo2.get()
    Color = combo3.get()
    ChassisNumber = en1.get()
    EngineNumber = en2.get()


    if combo5.get() == "Sold" :

        try:
            sql = "INSERT INTO penjualan VALUES (%s, %s, %s, %s, %s)"
            val = (Dealer, Type, Color, ChassisNumber, EngineNumber)
            cursor = db.cursor()
            cursor.execute(sql, val)
            cursor.close()
            db.commit()
        except:
            print("Cannot run command, please try again!")
        else:
            print("Thank You.")
            exit()
    else:
        print("Thank You, stock updated.")
        exit()

def comboclick(event):

    if combo2.get() == "TZ40" :
        combo3.config(value=TZ40_colors, state="disabled")
        combo3.current(0)
    if combo2.get() == "TW50" :
        combo3.config(value=TW50_colors, state="disabled")
        combo3.current(0)
    if combo2.get() == "TV50" :
        combo3.config(value=TV50_colors)
    if combo2.get() == "TR50" :
        combo3.config(value=TR50_colors, state="disabled")
        combo3.current(0)
    if combo2.get() == "TQ40" :
        combo3.config(value=TQ40_colors, state="disabled")
        combo3.current(0)
    if combo2.get() == "TM50" :
        combo3.config(value=TM50_colors, state="disabled")
        combo3.current(0)
    if combo2.get() == "TL50" :
        combo3.config(value=TL50_colors, state="disabled")
        combo3.current(0)
    if combo2.get() == "TK50" :
        combo3.config(value=TK50_colors, state="disabled")
        combo3.current(0)
    if combo2.get() == "TI40" :
        combo3.config(value=TI40_colors, state="disabled")
        combo3.current(0)
    if combo2.get() == "TH40" :
        combo3.config(value=TH40_colors, state="disabled")
        combo3.current(0)
    if combo2.get() == "TG40" :
        combo3.config(value=TG40_colors, state="disabled")
        combo3.current(0)
    if combo2.get() == "PT20" :
        combo3.config(value=PT20_colors, state="disabled")
        combo3.current(0)

options1 = []
sql1 = " SELECT Kode_Dealer FROM m_dealer"
cursor.execute(sql1)
Dealer = cursor.fetchall()
for i in Dealer:
    options1.append(str(i[0]))

options2 = []
sql2 = " SELECT Type FROM stock_kendaraan"
cursor.execute(sql2)
Type = cursor.fetchall()
for i in Type:
    options2.append(str(i[0]))

options3 = []
sql3 = " SELECT Product FROM stock_kendaraan"
cursor.execute(sql3)
Product = cursor.fetchall()
for i in Product:
    options3.append(str(i[0]))

options4 = []
sql4 = " SELECT COLOR FROM m_color"
cursor.execute(sql4)
Color = cursor.fetchall()
for i in Color:
    options4.append(str(i[0]))

# List of types
types = [
    "TZ40",
    "TW50",
    "TV50",
    "TR50",
    "TQ40",
    "TM50",
    "TL50",
    "TK50",
    "TI40",
    "TH40",
    "TG40",
    "PT20"
]



root = Tk()

Dealer = StringVar()
Type = StringVar()
Product = StringVar()
ChassisNumber = StringVar()
EngineNumber = StringVar()
Color = StringVar()
Status = StringVar()

wrapper1 = LabelFrame(root, text="Choose Available Data You Wanted To Update")
wrapper1.pack(padx=10, pady=10, fill="both", expand="yes")

#Label1
label1 = Label(wrapper1, text="Dealer")
label1.grid(row=1, column=0, padx=10, pady=10)
combo1 = ttk.Combobox(wrapper1, textvariable=Dealer)
combo1['values'] = options1
combo1.grid(row=1, column=1, padx=10, pady=5)

#Label2
label2 = Label(wrapper1, text="Type")
label2.grid(row=2, column=0, padx=10, pady=10)
combo2 = ttk.Combobox(wrapper1, textvariable=Type)
combo2['values'] = types
combo2.grid(row=2, column=1, padx=10, pady=5)
combo2.bind("<<ComboboxSelected>>", comboclick)

#Label3
label3 = Label(wrapper1, text="Color")
label3.grid(row=3, column=0, padx=10, pady=10)
combo3 = ttk.Combobox(wrapper1, textvariable=Color)
combo3['values'] = [" ", " "]
combo3.grid(row=3, column=1, padx=10, pady=5)

#Label4
label4 = Label(wrapper1, text="Chassis Number")
label4.grid(row=4, column=0, padx=10, pady=10)
en1 = Entry(wrapper1, textvariable=ChassisNumber)
en1.grid(row=4, column=1, padx=10, pady=5)

#Label5
label5 = Label(wrapper1, text="Engine Number")
label5.grid(row=5, column=0, padx=10, pady=5)
en2 = Entry(wrapper1, textvariable=EngineNumber)
en2.grid(row=5, column=1, padx=10, pady=5)

#Label7
label7 = Label(wrapper1, text="Status Stock Update")
label7.grid(row=7, column=0, padx=10, pady=5)
combo5 = ttk.Combobox(wrapper1, textvariable=Status)
combo5['values'] = ("Stock" , "Sold")
combo5.grid(row=7, column=1, padx=10, pady=5)

combo5.bind("<<ComboboxSelected>>")

Button(root, text="UPDATE", command=Submit, height= 2, width= 10).place(x=160, y=300)

cursor.close()

root.geometry("400x400")
root.title("Update Status Stock Form")

root.mainloop()