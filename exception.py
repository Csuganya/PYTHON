try:
   fh = open("testfile", "r")
   fh.write("This is my test file for exception handling!!")
except IOError:
   print ("Error: can\'t find file or read data")
else:
   print ("Written content in the file successfully")
   fh.close()
finally:
    print("OK")

try:
    c=1/0
except (FloatingPointError,ZeroDivisionError):
    print("Error")
except Exception:
    print("All")
