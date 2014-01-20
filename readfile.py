f=open("D:/sg/temp.txt","r")
str=f.read(10)
print(str)
f.seek(5,0)
print(f.read(10))
#print(str)
 
