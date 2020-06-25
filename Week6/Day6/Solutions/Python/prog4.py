for i in range(4):
    for j in range(4):
        if i>j:
            print(" ",end="\t")
        else:
            print(str(i)+str(j),end="\t")
    print()
