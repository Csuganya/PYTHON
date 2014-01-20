
import mysql.connector
rno=eval(input("Enter regno:"))
name=input("Enter name:")
mark=input("Enter mark:"))
result=eval(input("pass"))
cn=mysql.connector.connect(user='root',database="student",password='root')
cr=cn.cursor()
cr.execute("Insert into mark(regno,name,mark,result)values({0}'{1}',{2},'{3}')".format(rno,name,mark,result))
  cn.commit()
  print("Record inserted")
  cr.close()
  cn.close()
