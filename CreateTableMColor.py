import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="STOCK_VEHICLE"
)

cursor = db.cursor()

sql = """CREATE TABLE m_color (
      COLOR_id VARCHAR(255),
      COLOR VARCHAR(255),
      KEY (COLOR_id)


      )
"""

try:
    cursor.execute(sql)
except:
    print("Table cannot be created, please try again!")
else:
    print("Table has been created.")


cursor.close()