for i in range(4):
    for j in range(4):
        if i+j<3:
            print("  ",end=" ")
        elif i+j==3:
            print("9",end=" ")
        else:
            print((i+j)*(i+j),end=" ")
    print()
