val = 65
for i in range(5):
    for j in range(3):
        if i+j < 2 or i-j > 2:
            print(" ",end=" ")
        else:
            print(chr(val),end=" ")
            val += 1
    print()
