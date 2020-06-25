val = 8
for i in range(7):
    for j in range(4):
        if i+j < 3 or i-j > 3:
            print(" ", end=" ")
        else:
            print(val, end=" ")
    if i < 3:
        val -= 2
    else:
        val += 2
    print()
