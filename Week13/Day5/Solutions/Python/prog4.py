a = 0
b = 4
for i in range(5):
    for j in range(5):
        if i == j or i+j == 4:
            print("X",end=" ")
        else:
            print(" ",end=" ")
    print()
