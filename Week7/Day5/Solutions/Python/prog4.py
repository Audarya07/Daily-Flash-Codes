
for i in range(4):
    num=0
    for j in range(4,i,-1):
        print(str(i+num)+chr(num+65),end="  ")
        num+=1
    print()

