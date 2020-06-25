for i in range(4):
    for j in range(4,i+1,-1):
       print(" ",end=" ")
    for k in range(i+1):
            print(chr(k+65),end=" ")
    print()
