#inserting the records to the table
import mysql.connector
from datetime import date, datetime, timedelta
#host='127.0.0.1' is mentioned the local system ip.
#If you want to connect another system database, mention the IP Address of the System
#example: (user='root' password='root' host='192.168.1.10' database='dbname')
cn = mysql.connector.connect(user='root', database='emp',password='root',host='127.0.0.1') #creating connection
cr = cn.cursor() #handle structure (like dataatapter)
tomorrow = datetime.now().date() + timedelta(days=1)
query="INSERT INTO employees(first_name, last_name, hire_date, gender, birth_date) VALUES('{}','{}','{}','{}','{}')".format("Arun","Kumar",tomorrow,'M',date(1988,9,24))
cr.execute(query)
emp_no = cr.lastrowid
#we retrieve the newly inserted value for the emp_no column (an AUTO_INCREMENT column) using the lastrowid property of the cursor object.
print("We Inserted the Employee Number of {0} ".format(emp_no))

# you must commit the data after a sequence of INSERT, DELETE, and UPDATE statements.
# Make sure data is committed to the database
cn.commit()
cr.close() #closing the cursor
cn.close() #closing the connection

