for i in range(4):
    for j in range(7):
        if i+j < 3 or j-i >= 4:
            print(" ",end=" ")
        else: 
            if j <= 3:
                a = j+1
                print(a,end=" ")   
            else:
                a -= 1
                print(a,end=" ")
    print()
