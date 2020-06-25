val = 4
a = 66
for i in range(val, -val, -1):
    b = a
    for j in range(1, abs(i) + 1):
        print(" ",end=" ")
    for k in range(val, abs(i), -1):
        print(chr(b)+"  ",end=" ")
        b += 1
    a = b-1
    print()
