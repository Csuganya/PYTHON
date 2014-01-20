mport mysql.connector
cn=mysql.connector.connect(user='root',database="student",password='root')
cr=cn.cursor()
cr.execute("select * from mark")
for(r,n,m,rs) in cr:
 print("{0:<5}|{1:^20}|{2:<}|{3:>10}|".format(r,n,m,rs))
cr.close()
cn.close()
