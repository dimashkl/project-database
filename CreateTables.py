import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="STOCK_VEHICLE"
)

cursor = db.cursor()
sql = """CREATE TABLE m_dealer (
      DEALER_id INT,
      Nama_Dealer VARCHAR(255),
      Kode_Dealer VARCHAR(3),
      Alamat VARCHAR(255),
      NoTelp VARCHAR(15),
      FAX VARCHAR(15),
      Email VARCHAR(255),
      NPWP VARCHAR(255),
      Actived VARCHAR(255),
      KEY (DEALER_id)
      
      
      )
"""

try :
  cursor.execute(sql)
except :
  print("Table cannot be created, please try again!")
else :
  print("Table has been created.")

cursor.close()