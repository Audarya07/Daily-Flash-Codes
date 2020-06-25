num2 = 0
for i in range(4):
    num = num2
    for j in range(4):
        if i>j:
            print(" ",end="\t")
        else:
            print(str(bin(num))[2:],end="\t")
            num+=1
    num2+=2
    print()
