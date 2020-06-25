a = 0
for i in range(4):
    for j in range(7):
        if i > j or i+j > 6:
            print(" ",end=" ")
        else:
            print(a,end=" ")
            a += 1
    a = (i+1)*(i+2)
    print()
