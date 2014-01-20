def matrixmul(a,b):
 for i in range(2):
  for j in range(2):
   for k in range(2):
    c=a[i][j]*b[j][i]
   print(" ",c,end=' ')
  print()
