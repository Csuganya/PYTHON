for i in range(10):
 c=1
 for j in range(10-i):
  print("  ",end='')
 for k in range(i+1):
  print(" "+str(int(c))+" ",end='')
  c=c*(i-k)/(k+1);
 print()
pass
