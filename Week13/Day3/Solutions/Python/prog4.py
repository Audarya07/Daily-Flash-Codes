val = 4
for i in range(val, -val, -1):
    for j in range(1, abs(i) + 1):
        print(" ",end=" ")
    for k in range(val, abs(i), -1):
        print("1  ",end=" ")
    print()
