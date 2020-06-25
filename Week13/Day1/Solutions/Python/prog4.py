a = 3
for i in range(7):
    flag = 0
    cnt = i+1
    for j in range(7):
        if i+j < 3 or j-i > 3 or i-j > 3 or i+j > 9:
            print(" ",end=" ")
        else:
            if i < 4:
                flag = 0
                print(cnt,end=" ")
            else:
                flag = 1
                print(a,end=" ")
    if flag == 1:
        a -= 1
                 
    print()
