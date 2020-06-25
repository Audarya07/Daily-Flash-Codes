cnt = 1

for i in range(7):
    for j in range(4):
        if j > i or i+j >=7:
            print(" ",end=" ")
        elif i<4:
            print(cnt,end=" ")
            cnt += 1
        else:
            cnt-=1
            print(cnt-1,end=" ")
    print()
