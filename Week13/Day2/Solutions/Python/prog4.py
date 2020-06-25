a = 3
val = 65
for i in range(7):
    flag = 0
    cnt = i+1
    for j in range(7):
        if i+j < 3 or j-i > 3 or i-j > 3 or i+j > 9:
            print(" ",end=" ")
        else:
            if i < 4:
                if i%2 == 0:
                    print(i+1,end=" ")
                if i == 1:
                    print("A",end=" ")
                if i == 3:
                    print("B",end=" ")
            else:
                flag = 1
                if i%2 == 0:
                    print(a,end=" ")
                else:
                    print("A",end=" ")
    if flag == 1:
        a -= 1
    if flag == 0:
        val += 1
                 
    print()
