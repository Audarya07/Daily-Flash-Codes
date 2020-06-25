l=5
for i in range(4):
    m=l
    k=1
    for j in range(4):
        if j>=i:
            print(k,end=" ")
            k+=1
        else:
            print(m,end=" ")
            m+=1
    l-=1
    print()

