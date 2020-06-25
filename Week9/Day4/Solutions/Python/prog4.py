cnt = 1
for i in range(4):
    for j in range(7):
        if i > j or i+j > 6:
            print(" ",end=" ")
        else:
            if i%2 == 0:
                print(cnt,end=" ")
                cnt += 1
            else:
                print(cnt,end=" ")
                cnt -= 1
    if i%2==0:
        cnt-=1
    else:
        cnt+=1
    print()
