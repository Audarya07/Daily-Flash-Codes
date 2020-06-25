for i in range(4):
    for k in range(4,i+1,-1):
        print(" ",end=" ")
    for j in range(i+1):
        print(chr(i+65),end=" ")
        i-=1
    i+=1
    print()
