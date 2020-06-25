for i in range(4):
    for j in range(4,i,-1):
        if j%2!=0:
            print("=",end=" ")
        else:
            print("+",end=" ")
    print()
