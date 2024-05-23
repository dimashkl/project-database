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

#Trigger Insert After

sql = "CREATE TRIGGER Trigger_mkendaraan" \
      "     AFTER insert" \
      "     on m_kendaraan" \
      "     for each row" \
      "BEGIN" \
      "     INSERT INTO penjualan;" \
      "END"

try :
    cursor.execute(sql)
except :
    print("Cannot make any trigger. Try again.")
else :
    print("Trigger created")

cursor.close()
