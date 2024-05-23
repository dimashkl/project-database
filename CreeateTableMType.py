import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="STOCK_VEHICLE"
)

cursor = db.cursor()

sql = """CREATE TABLE m_type (
      TYPE_id VARCHAR(255),
      Product VARCHAR(255),
      KEY (TYPE_id)


      )
"""

try:
    cursor.execute(sql)
except:
    print("Table cannot be created, please try again!")
else:
    print("Table has been created.")


cursor.close()