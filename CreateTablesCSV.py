import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="STOCK_VEHICLE"
)

cursor = db.cursor()
sql = """CREATE TABLE m_kendaraan (
      kendaraan_id INT AUTO_INCREMENT PRIMARY KEY,
      DEALER_id INT,
      PurchaseOrderNO VARCHAR(255),
      PurchaseReceiptNO VARCHAR(255),
      TransactionDate VARCHAR(255),
      VENDOR VARCHAR(255),
      DeliveryDate VARCHAR(255),
      no_DO VARCHAR(255) ,
      DealerPurchaseNO VARCHAR(255),
      no_SO VARCHAR(255),
      CHASSIS_NUMBER VARCHAR(255),
      ENGINE_NUMBER VARCHAR(255),
      Product VARCHAR(255),
      TYPE_id VARCHAR(255),
      COLOR VARCHAR(255),
      COLOR_id VARCHAR(255),
      KEY (DEALER_id),
      KEY (TYPE_id)
      )
"""

try :
  cursor.execute(sql)
except :
  print("Table cannot be created, please try again!")
else :
  print("Table has been created.")

cursor.close()