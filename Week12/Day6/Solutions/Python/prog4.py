num = 9
for i in range(4):
    for j in range(7):
        if i > j or i + j >= 7:
            print(" ",end=" ")
        else:
            if j <= 3:
                num -= 1
                print(num,end=" ")
                
            else:
                num += 1
                print(num,end=" ")
    print()
