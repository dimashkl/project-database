import mysql.connector
import csv
import pandas as pd

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="STOCK_VEHICLE"
)

cursor = db.cursor()

file = open('Purchase Receipt Detail V1.csv')
csv_data = csv.reader(file)

count = 0
for row in csv_data:
    if count < 1:
        continue
    else :
            cursor.execute("INSERT INTO STOCK_VEHICLE.m_kendaraan (kendaraan_id, DEALER_id, PurchaseOrderNO, PurchaseReceiptNO, TranscationDate, VENDOR, "
                   "Delivery Date, no_DO, DeliveryPurchaseNO, no_SO, CHASSIS_NUMBER. ENGINE_NUMBER, PRODUCT, TYPE_id, COLOR, COLORD_id)"
                   "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", row)

cursor.close()

db.commit()

print("Import Successfull!")