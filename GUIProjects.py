from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import DateEntry
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="STOCK_VEHICLE"
)

cursor = db.cursor()

def SaveStatus():
    DEALER_id = combo1.get()
    PurchaseOrderNumber = en2.get()
    PurchaseReceiptNumber = en3.get()
    TransactionDate = cal.get()
    Vendor = en4.get()
    DeliveryDate = cal1.get()
    DeliveryOrderNumber = en5.get()
    DealerPurchaseNumber = en6.get()
    SalesOrderNumber = en7.get()
    ChassisNumber = en8.get()
    EngineNumber = en9.get()
    Product = combo2.get()
    Type = combo3.get()
    KodeWarna = combo4.get()
    Warna = combo5.get()

    sql = "INSERT INTO m_penjualan (DEALER_id,PurchaseOrderNO,PurchaseReceiptNO,TransactionDate,VENDOR,DeliveryDate,no_DO,DealerPurchaseNO,no_SO,CHASSIS_NUMBER,ENGINE_NUMBER,PRODUCT,TYPE_id,COLOR,COLOR_id)" \
          "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val = ("", DEALER_id, PurchaseOrderNumber, PurchaseReceiptNumber, TransactionDate, Vendor,
           DeliveryDate, DeliveryOrderNumber, DealerPurchaseNumber, SalesOrderNumber, ChassisNumber, EngineNumber,
           Product, Type, KodeWarna, Warna)

    try:
        cursor.execute(sql, val)
        cursor.execute(messagebox.showinfo("Data Records", "Successfully added a new data!"))
        cursor.close()
        print("Thank You")
    except:
        print("Thank You.")

options = []
sql0 = " SELECT DEALER_id, Nama_Dealer FROM m_dealer"
cursor.execute(sql0)
ids = cursor.fetchall()
for i in ids:
    options.append(str(i[0])+" - "+i[1])

options1 = []
sql1 = " SELECT Product FROM m_type"
cursor.execute(sql1)
product = cursor.fetchall()
for i in product:
    options1.append(str(i[0]))

options2 = []
sql2 = " SELECT TYPE_id FROM m_type"
cursor.execute(sql2)
type = cursor.fetchall()
for i in type:
    options2.append(str(i[0]))

options3 = []
sql3 = " SELECT COLOR_id FROM m_color"
cursor.execute(sql3)
colorid = cursor.fetchall()
for i in colorid:
    options3.append(str(i[0]))

options4 = []
sql4 = " SELECT COLOR FROM m_color"
cursor.execute(sql4)
color = cursor.fetchall()
for i in color:
    options4.append(str(i[0]))

options5 = []
sql5 = " "

root = Tk()

alpha = StringVar()
alabel = StringVar()
blabel = StringVar()
clabel = StringVar()
dlabel = StringVar()
elabel = StringVar()
flabel = StringVar()
glabel = StringVar()
hlabel = StringVar()
ilabel = StringVar()
jlabel = StringVar()
klabel = StringVar()
llabel = StringVar()
mlabel = StringVar()
nlabel = StringVar()

wrapper1 = LabelFrame(root, text="Input New Data")
#wrapper2 = LabelFrame(root, text="Stock Vehicle Update")
wrapper1.pack(padx=10, pady=10, fill="both", expand="yes")
#wrapper2.pack(padx=10, pady=10, fill="both", expand="yes")

#Label(wrapper1, text="Please select the correct data!").grid(row=0, column=0, padx=10, pady=10)

#Label1
label1 = Label(wrapper1, text="Dealer ID")
label1.grid(row=1, column=0, padx=10, pady=10)
combo1 = ttk.Combobox(wrapper1, textvariable=alabel)
combo1['values'] = options
combo1.grid(row=1, column=1, padx=10, pady=10)
combo1.current(0)
#Label2
label2 = Label(wrapper1, text="Purchase Order Number")
label2.grid(row=2, column=0, padx=10, pady=5)
en2 = Entry(wrapper1, textvariable=blabel)
en2.grid(row=2, column=1, padx=10, pady=5)
#Label3
label3 = Label(wrapper1, text="Purchase Receipt Number")
label3.grid(row=3, column=0, padx=10, pady=5)
en3 = Entry(wrapper1, textvariable=clabel)
en3.grid(row=3, column=1, padx=10, pady=5)
#Label4
label4 = Label(wrapper1, text="Transaction Date")
label4.grid(row=4, column=0, padx=10, pady=5)
cal = DateEntry(wrapper1, width=12, year=2022, month=6, day=22, background='darkblue', foreground='white', borderwidth=2)
cal.grid(row=4, column=1, padx=10, pady=10)
#Label5
label5 = Label(wrapper1, text="Vendor")
label5.grid(row=5, column=0, padx=10, pady=5)
en4 = Entry(wrapper1, textvariable=dlabel)
en4.grid(row=5, column=1, padx=10, pady=5)
#Label6
label6 = Label(wrapper1, text="Delivery Date")
label6.grid(row=6, column=0, padx=10, pady=5)
cal1 = DateEntry(wrapper1, width=12, year=2022, month=6, day=22, background='darkblue', foreground='white', borderwidth=2)
cal1.grid(row=6, column=1, padx=10, pady=10)
#Label7
label7 = Label(wrapper1, text="Delivery Order Number")
label7.grid(row=7, column=0, padx=10, pady=5)
en5 = Entry(wrapper1, textvariable=elabel)
en5.grid(row=7, column=1, padx=10, pady=5)
#Label8
label8 = Label(wrapper1, text="Dealer Purchase Number")
label8.grid(row=8, column=0, padx=10, pady=5)
en6 = Entry(wrapper1, textvariable=flabel)
en6.grid(row=8, column=1, padx=10, pady=5)
#Label9
label9 = Label(wrapper1, text="Sales Order Number")
label9.grid(row=9, column=0, padx=10, pady=5)
en7 = Entry(wrapper1, textvariable=glabel)
en7.grid(row=9, column=1, padx=10, pady=5)
#Label10
label10 = Label(wrapper1, text="Chassis Number")
label10.grid(row=10, column=0, padx=10, pady=5)
en8 = Entry(wrapper1, textvariable=hlabel)
en8.grid(row=10, column=1, padx=10, pady=5)
#Label11
label11 = Label(wrapper1, text="Engine Number")
label11.grid(row=11, column=0, padx=10, pady=5)
en9 = Entry(wrapper1, textvariable=ilabel)
en9.grid(row=11, column=1, padx=10, pady=5)
#Label12
label12 = Label(wrapper1, text="Product")
label12.grid(row=12, column=0, padx=10, pady=5)
combo2 = ttk.Combobox(wrapper1, textvariable=jlabel)
combo2['values'] = options1
combo2.grid(row=12, column=1, padx=10, pady=5)
#Label13
label13 = Label(wrapper1, text="Type Kendaraan")
label13.grid(row=13, column=0, padx=10, pady=5)
combo3 = ttk.Combobox(wrapper1, textvariable=klabel)
combo3['values'] = options2
combo3.grid(row=13, column=1, padx=10, pady=5)
#Label14
label14 = Label(wrapper1, text="Kode Warna")
label14.grid(row=14, column=0, padx=10, pady=5)
combo4 = ttk.Combobox(wrapper1, textvariable=llabel)
combo4['values'] = options3
combo4.grid(row=14, column=1, padx=10, pady=5)
#Label15
label15 = Label(wrapper1, text="Warna")
label15.grid(row=15, column=0, padx=10, pady=5)
combo5 = ttk.Combobox(wrapper1, textvariable=mlabel)
combo5['values'] = options4
combo5.grid(row=15, column=1, padx=10, pady=5)
#Label16
label16 = Label(wrapper1, text="Select Status")
label16.grid(row=16, column=0, padx=10, pady=5)
combo6 = ttk.Combobox(wrapper1, textvariable=nlabel)
combo6['values'] = ['Available', 'Pending', 'On Delivery','Sold']
combo6.grid(row=16, column=1, padx=10, pady=5)

Button(root, text="SUBMIT", command=SaveStatus, height= 2, width= 10).place(x=160, y=530)


root.geometry("400x600")
root.title("Data Entry Form")

root.mainloop()