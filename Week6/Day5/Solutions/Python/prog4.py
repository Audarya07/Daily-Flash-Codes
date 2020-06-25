l = ['C','O','R','E']
for i in range(len(l)):
    for j in range(len(l)):
        if i>j:
            print(" ",end=" ")
        else:
            print(l[j],end=" ")
    print()
