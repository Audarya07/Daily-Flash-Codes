for i in range(5):
    cnt=0
    for j in range(5):
        if i>j:
            print(" ",end=" ")
            cnt+=1
        else:
            print((i+cnt)*cnt,end=" ")
            cnt+=1
    print()
