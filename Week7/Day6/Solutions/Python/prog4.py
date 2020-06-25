for i in range(4):
    for j in range(4):
        if i+j>=4:
            print(" ",end=" ")
        else:
            if j%2==0:
                print("0",end=" ")
            else:
                print("1",end=" ")
    print()
