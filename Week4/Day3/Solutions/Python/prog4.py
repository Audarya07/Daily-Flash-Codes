num = 97
x = 2
for i in range(4):
    for j in range(4-i):
        print(chr(num),end=" ")
        num+=1
    num-=x
    x-=1
    print()
