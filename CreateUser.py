import pymysql

def getDatabaseConnection(ipaddress, usr, passwd, charset, curtype):
    sqlCon  = pymysql.connect(host=ipaddress, user=usr, password=passwd, charset=charset, cursorclass=curtype);
    return sqlCon

def createUser(cursor, userName, password,
               querynum=0,
               updatenum=0,
               connection_num=0):
    """try :
        sqlCreateUser = "CREATE USER 'suryaputra'@'127.0.0.1' IDENTIFIED BY 'spsarana';" %(userName, password)
        cursor.execute(sqlCreateUser)
    except Exception as Ex :
        print("Error creating User."%(Ex))
    else :
        print("User created!")"""

ipaddress   = "127.0.0.1"
usr         = "root"
passwd      = ""
charset     = "utf8mb4"
curtype    = pymysql.cursors.DictCursor

mySQLConnection = getDatabaseConnection(ipaddress, usr, passwd, charset, curtype)
mySQLCursor     = mySQLConnection.cursor()

createUser(mySQLCursor, "surput","suryaputra")
createUser(mySQLCursor, "suryaputra", "spsarana")

mySqlListUsers = "select host, user from mysql.user;"
mySQLCursor.execute(mySqlListUsers)

userList = mySQLCursor.fetchall()

print("List of users:")
for user in userList:
    print(user)

