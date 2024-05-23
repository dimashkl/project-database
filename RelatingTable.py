import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="STOCK_VEHICLE"
)

cursor = db.cursor()

relation = ('ALTER TABLE m_kendaraan ADD foreign key(DEALER_id) references m_dealer(DEALER_id)')

try :
    cursor.execute(relation)
except :
    print("Relation can't be reached.")
else :
    print("Relation created.")
