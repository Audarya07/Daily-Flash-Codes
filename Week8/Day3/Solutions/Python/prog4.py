a = 0
b = 1
for i in range(4):
    for j in range(7):
        if i+j < 3 or j-i >= 4:
            print(" ",end=" ")
        else:
            print(a,end=" ")
            c = a+b
            a=b
            b=c
    print()
