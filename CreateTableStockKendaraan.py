import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="STOCK_VEHICLE"
)

cursor = db.cursor()
sql = """CREATE TABLE stock_kendaraan (
      ID INT AUTO_INCREMENT PRIMARY KEY,
      Type VARCHAR(255),
      Product VARCHAR(255),
      Stock INT,
      KEY (Type)
      )
"""

#---DATA STOCK PER-TYPE
TZ40 = """CREATE TABLE TZ40 (
       Dealer VARCHAR(255),
       Type VARCHAR(255),
       Product VARCHAR(255),
       Chassis_Number VARCHAR(255),
       Engine_Number VARCHAR(255),
       Color VARCHAR(255),
       KEY (Type)
       )
       """
TW50 = """CREATE TABLE TW50 (
       Dealer VARCHAR(255),
       Type VARCHAR(255),
       Product VARCHAR(255),
       Chassis_Number VARCHAR(255),
       Engine_Number VARCHAR(255),
       Color VARCHAR(255),
       KEY (Type)
       )
       """
TV50 = """CREATE TABLE TV50 (
       Dealer VARCHAR(255),
       Type VARCHAR(255),
       Product VARCHAR(255),
       Chassis_Number VARCHAR(255),
       Engine_Number VARCHAR(255),
       Color VARCHAR(255),
       KEY (Type)
       )
       """
TR50 = """CREATE TABLE TR50 (
       Dealer VARCHAR(255),
       Type VARCHAR(255),
       Product VARCHAR(255),
       Chassis_Number VARCHAR(255),
       Engine_Number VARCHAR(255),
       Color VARCHAR(255),
       KEY (Type)
       )
       """
TQ40 = """CREATE TABLE TQ40 (
       Dealer VARCHAR(255),
       Type VARCHAR(255),
       Product VARCHAR(255),
       Chassis_Number VARCHAR(255),
       Engine_Number VARCHAR(255),
       Color VARCHAR(255),
       KEY (Type)
       )
       """
TM50 = """CREATE TABLE TM50 (
       Dealer VARCHAR(255),
       Type VARCHAR(255),
       Product VARCHAR(255),
       Chassis_Number VARCHAR(255),
       Engine_Number VARCHAR(255),
       Color VARCHAR(255),
       KEY (Type)
       )
       """
TL50 = """CREATE TABLE TL50 (
       Dealer VARCHAR(255),
       Type VARCHAR(255),
       Product VARCHAR(255),
       Chassis_Number VARCHAR(255),
       Engine_Number VARCHAR(255),
       Color VARCHAR(255),
       KEY (Type)
       )
       """
TK50 = """CREATE TABLE TK50 (
       Dealer VARCHAR(255),
       Type VARCHAR(255),
       Product VARCHAR(255),
       Chassis_Number VARCHAR(255),
       Engine_Number VARCHAR(255),
       Color VARCHAR(255),
       KEY (Type)
       )
       """
TI40 = """CREATE TABLE TI40 (
       Dealer VARCHAR(255),
       Type VARCHAR(255),
       Product VARCHAR(255),
       Chassis_Number VARCHAR(255),
       Engine_Number VARCHAR(255),
       Color VARCHAR(255),
       KEY (Type)
       )
       """
TH40 = """CREATE TABLE TH40 (
       Dealer VARCHAR(255),
       Type VARCHAR(255),
       Product VARCHAR(255),
       Chassis_Number VARCHAR(255),
       Engine_Number VARCHAR(255),
       Color VARCHAR(255),
       KEY (Type)
       )
       """
TG40 = """CREATE TABLE TG40 (
       Dealer VARCHAR(255),
       Type VARCHAR(255),
       Product VARCHAR(255),
       Chassis_Number VARCHAR(255),
       Engine_Number VARCHAR(255),
       Color VARCHAR(255),
       KEY (Type)
       )
       """
PT20 = """CREATE TABLE PT20 (
       Dealer VARCHAR(255),
       Type VARCHAR(255),
       Product VARCHAR(255),
       Chassis_Number VARCHAR(255),
       Engine_Number VARCHAR(255),
       Color VARCHAR(255),
       KEY (Type)
       )
       """

try :
  cursor.execute(sql)
  cursor.execute(TZ40)
  cursor.execute(TW50)
  cursor.execute(TV50)
  cursor.execute(TR50)
  cursor.execute(TQ40)
  cursor.execute(TM50)
  cursor.execute(TL50)
  cursor.execute(TK50)
  cursor.execute(TI40)
  cursor.execute(TH40)
  cursor.execute(TG40)
  cursor.execute(PT20)
except :
  print("Table cannot be created, please try again!")
else :
  print("Table has been created.")

cursor.close()