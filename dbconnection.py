#Proper database connecting
import mysql.connector
from mysql.connector import errorcode
try:
  cn = mysql.connector.connect(user='root', host='127.0.0.1', password='root', database='testt')
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exists")
  else:
    print(err)
else:
  cn.close()
