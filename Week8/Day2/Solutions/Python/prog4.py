for i in range(4):
    val = 65
    cnt = 0
    for j in range(7):
        if i+j < 3 or j-i >= 4:
            print(" ",end=" ")
        else:
            print(chr(val+cnt),end=" ")
            cnt+=1
    print()
