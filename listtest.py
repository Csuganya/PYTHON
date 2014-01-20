def inputList():
    dim=eval(input("Enter Dimension of Matrix"))

    a=[]
    chn=""
    while(chn != "."):
        ch=input("Enter No for List : ")
        for i in range(dim):
            for j in range(dim):
                a[i][j]=eval(chn)
    return a


a=inputList()
for i in range (3):
    for j in range(3):
        print(a[i][j],end="")
    print()
