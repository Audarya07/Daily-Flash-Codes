x=7
for i in range(4):
    n=x
    for j in range(i+1):
        print(n,end=" ")
        n-=1
    print()
    x-=1
