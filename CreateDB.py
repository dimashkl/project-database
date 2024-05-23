import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd=""
)

cursor = db.cursor()
cursor.execute("DROP DATABASE STOCK_KENDARAAN")
#cursor.execute("CREATE DATABASE stock_vehicle")
print('Database has been successfully created!')

