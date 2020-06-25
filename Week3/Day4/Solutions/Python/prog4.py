x = 7
for i in range(4):
    for j in range(i+1):
        print(x,end=" ")
        x-=1
    x+=1
    print()
