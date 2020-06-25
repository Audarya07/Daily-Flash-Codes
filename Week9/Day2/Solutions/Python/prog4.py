for i in range(4):
    for j in range(7):
        if i > j or i+j > 6:
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()
