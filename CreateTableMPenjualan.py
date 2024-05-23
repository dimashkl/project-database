import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="STOCK_VEHICLE"
)

cursor = db.cursor()
sql = """CREATE TABLE penjualan (
      Dealer VARCHAR(255),
      Type VARCHAR(255),
      Color VARCHAR(255),
      Chassis_Number VARCHAR(255),
      Engine_Number VARCHAR(255)
      )
"""

try :
  cursor.execute(sql)
except :
  print("Table cannot be created, please try again!")
else :
  print("Table has been created.")

cursor.close()