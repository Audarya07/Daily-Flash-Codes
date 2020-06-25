for i in  range(5):
    for j in range(5):
        if i==0:
            print("0",end=" ")
        elif i>j:
            print(" ",end=" ")
        else:
            print(i*j,end=" ")
    print()
