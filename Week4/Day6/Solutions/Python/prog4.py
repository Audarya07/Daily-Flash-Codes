a = 0
b = 1
for i in range(4):
    for j in range(4):
        if i+j == 3:
            print("=",end=" ")
        elif i+j < 3:
            print(" ",end=" ")
        else:
            c=a+b
            a=b
            b=c
            print(a,end=" ")
    print()
