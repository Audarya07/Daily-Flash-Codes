num = 3
for i in range(4):
    for j in range(4):
        if i+j<3:
            print(" ",end=" ")
        elif i+j==3:
            print("3",end=" ")
        elif i+j==4:
            print(4*j,end=" ")
        elif i+j==5:
            print(5*j,end=" ")
        elif i+j==6:
            print(6*j,end=" ")
    print()
