val = 65
for i in range(4):
    for j in range(1,5-i):
            print(chr(val),end=" ")
            val+=j
    val-=j
    print()
