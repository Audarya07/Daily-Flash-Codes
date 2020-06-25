k = 64
for i in range(1, 6):
    for j in range(3, 0,-1):
        if j <= i and i <= 3:
            k+=1
            print(chr(k), end = " ")
        elif i > 3 and j <= 6-i:
            k-=1
            print(chr(k),end = " ")
        else:
            print(" ",end=" ")
    print()
