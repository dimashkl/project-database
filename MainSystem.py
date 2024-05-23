import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=""
)

if db.is_connected():
    print("Connected to MySQL Successfully!")

cursor = db.cursor()

def menu():
    print("*** WELCOME TO DATABASE SYSTEM ***")
    print("1. Create Database")
    print("2. Create Master Table")
    print("3. Create User Privileges")
    print("4. Relating Tables")
    print("5. Quit.")

def databases():
    print("STOCK_VEHICLE")

def tables():
    print("m_kendaraan")
    print("m_dealer")

menu()
option = int(input("Input your choices : "))

while option !=0:
    if option == 1:
        databases()
        databases = str(input("Please input your database name : "))
        if databases == "STOCK_VEHICLE":
            try :
                cursor.execute("CREATE DATABASE STOCK_VEHICLE")
            except :
                print("Database can't be created. Please try again!")
            else :
                print("Database created.")
        else :
            print("Invalid option, please input the right option!")
        databases()
        databases = str(input("Please input your database name : "))
    elif option == 2:
        tables()
        tables = str(input("Please input your tables choices name : "))
            if tables == "m_kendaraan":
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
                         KEY (DEALER_id)
                         )
                     """

                try :
                    cursor.execute(sql)
                except :
                    print("Table cannot be created, please try again!")
                else :
                    print("Table has been created.")
            elif tables == "m_dealer":
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

                try:
                    cursor.execute(sql)
                except:
                    print("Table cannot be created, please try again!")
                else:
                    print("Table has been created.")
            else :
                print("Invalid Option.")
        tables()
        tables = str(input("Please input your tables choices name : "))
    elif option == 3:
        try:
            sqlCreateUser = "CREATE USER '%s'@'localhost' IDENTIFIED BY '%s';" % (userName, password)
            cursor.execute(sqlCreateUser)
        except Exception as Ex:
            print("Error creating User." % (Ex))
        else:
            print("User created!")
    elif option == 4:
