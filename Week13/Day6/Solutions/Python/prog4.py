for i in range(10):
    if i <= 5:
        for j in range(10):
            if j>i and i+j<9:
                print(" ",end=" ")
            else:
                print("*",end=" ")
    else:
        for j in range(10):
            if i+j<10 or i<=j:
                print("*",end=" ")
            else:
                print(" ",end=" ")
    print()
