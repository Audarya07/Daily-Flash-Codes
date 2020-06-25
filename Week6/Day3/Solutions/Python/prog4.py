cap = 69
small = 97
for i in range(4):
    for j in range(4):
        if i>j:
            print(" ",end=" ")
        elif j%2==0:
            print(chr(cap),end=" ")
            cap-=1
        elif j%2!=0:
            print(chr(small),end=" ")
            small+=1
    print()
