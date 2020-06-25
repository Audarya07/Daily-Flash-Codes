val = 1
for i in range(1,5):
    for j in range(i):
        print(val**3,end="  ")
        val+=1
    print()
