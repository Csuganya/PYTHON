try:
 c="a"/0
except (TypeError):
 print("Divided by zero")
else:
 print("No Error")
finally:
 print("Program Executed")
