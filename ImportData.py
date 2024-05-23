import csv
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="STOCK_VEHICLE"
)

cursor = db.cursor()

#OpenFileResources

file = open('Purchase Receipt Detail V1.csv')
csv_data = csv.reader(file)

data = open('Data Dealer.csv')
csv_data1 = csv.reader(data)

file1 = open('Data Type.csv')
csv_data2 = csv.reader(file1)

file2 = open('Data Color.csv')
csv_data3 = csv.reader(file2)

file3 = open('Data Stock.csv')
csv_data4 = csv.reader(file3)

#LoadDataUtama

stock = "LOAD DATA INFILE 'C:/Users/User/PycharmProjects/pythonProject/Data Stock.csv' INTO TABLE stock_kendaraan FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 LINES (ID, Type, Product, Stock)"

query = "LOAD DATA INFILE 'C:/Users/User/PycharmProjects/pythonProject/Purchase Receipt Detail V1.csv' INTO TABLE m_kendaraan FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 LINES (DEALER_id,PurchaseOrderNO,PurchaseReceiptNO,TransactionDate,VENDOR,DeliveryDate,no_DO,DealerPurchaseNO,no_SO,CHASSIS_NUMBER,ENGINE_NUMBER,PRODUCT,TYPE_id,COLOR,COLOR_id)"

values = "LOAD DATA INFILE 'C:/Users/User/PycharmProjects/pythonProject/Data Dealer.csv' INTO TABLE m_dealer FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 LINES (DEALER_id,Nama_Dealer,Kode_Dealer,Alamat,NoTelp,FAX,Email,NPWP,Actived)"

types = "LOAD DATA INFILE 'C:/Users/User/PycharmProjects/pythonProject/Data Type.csv' INTO TABLE m_type FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 LINES (TYPE_id, Product)"

color = "LOAD DATA INFILE 'C:/Users/User/PycharmProjects/pythonProject/Data Color.csv' INTO TABLE m_color FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 LINES (COLOR_id, COLOR)"

#LoadDataContohStockKendaraan

TZ40 = "LOAD DATA INFILE 'C:/Users/User/PycharmProjects/pythonProject/TZ40.csv' INTO TABLE TZ40 FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 LINES (Dealer,Type, Product, Chassis_Number, Engine_Number, Color)"

TW50 = "LOAD DATA INFILE 'C:/Users/User/PycharmProjects/pythonProject/TW50.csv' INTO TABLE TW50 FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 LINES (Dealer,Type, Product, Chassis_Number, Engine_Number, Color)"

TV50 = "LOAD DATA INFILE 'C:/Users/User/PycharmProjects/pythonProject/TV50.csv' INTO TABLE TV50 FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 LINES (Dealer,Type, Product, Chassis_Number, Engine_Number, Color)"

TR50 = "LOAD DATA INFILE 'C:/Users/User/PycharmProjects/pythonProject/TR50.csv' INTO TABLE TR50 FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 LINES (Dealer,Type, Product, Chassis_Number, Engine_Number, Color)"

TQ40 = "LOAD DATA INFILE 'C:/Users/User/PycharmProjects/pythonProject/TQ40.csv' INTO TABLE TQ40 FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 LINES (Dealer,Type, Product, Chassis_Number, Engine_Number, Color)"

TM50 = "LOAD DATA INFILE 'C:/Users/User/PycharmProjects/pythonProject/TM50.csv' INTO TABLE TM50 FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 LINES (Dealer,Type, Product, Chassis_Number, Engine_Number, Color)"

TL50 = "LOAD DATA INFILE 'C:/Users/User/PycharmProjects/pythonProject/TL50.csv' INTO TABLE TL50 FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 LINES (Dealer,Type, Product, Chassis_Number, Engine_Number, Color)"

TK50 = "LOAD DATA INFILE 'C:/Users/User/PycharmProjects/pythonProject/TK50.csv' INTO TABLE TK50 FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 LINES (Dealer,Type, Product, Chassis_Number, Engine_Number, Color)"

TI40 = "LOAD DATA INFILE 'C:/Users/User/PycharmProjects/pythonProject/TI40.csv' INTO TABLE TI40 FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 LINES (Dealer,Type, Product, Chassis_Number, Engine_Number, Color)"

TH40 = "LOAD DATA INFILE 'C:/Users/User/PycharmProjects/pythonProject/TH40.csv' INTO TABLE TH40 FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 LINES (Dealer,Type, Product, Chassis_Number, Engine_Number, Color)"

TG40 = "LOAD DATA INFILE 'C:/Users/User/PycharmProjects/pythonProject/TG40.csv' INTO TABLE TG40 FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 LINES (Dealer,Type, Product, Chassis_Number, Engine_Number, Color)"

PT20 = "LOAD DATA INFILE 'C:/Users/User/PycharmProjects/pythonProject/PT20.csv' INTO TABLE PT20 FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 LINES (Dealer,Type, Product, Chassis_Number, Engine_Number, Color)"

try :
    #cursor.execute(stock)
    #cursor.execute(query)
    cursor.execute(values)
    cursor.execute(types)
    cursor.execute(color)
    #cursor.execute(TZ40)
    #cursor.execute(TW50)
    #cursor.execute(TV50)
    #cursor.execute(TR50)
    #cursor.execute(TQ40)
    #cursor.execute(TM50)
    #cursor.execute(TL50)
    #cursor.execute(TK50)
    #cursor.execute(TI40)
    #cursor.execute(TH40)
    #cursor.execute(TG40)
    #cursor.execute(PT20)
except :
    print("Data cannot be imported!Please try again!")
else :
    print("Data has been imported successfully!")

db.commit()

cursor.close()
