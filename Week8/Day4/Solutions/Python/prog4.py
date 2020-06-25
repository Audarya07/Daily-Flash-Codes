for i in range(4):
    for j in range(7):
        if i+j < 3 or j-i >= 4:
            print(" ",end=" ")
        else:
            print(chr(65+j),end=" ")
    print()
