a = 65
for i in range(7):
    for j in range(4):
        if j > i or i+j >= 7:
            print(" ",end=" ")
        else:
            print(chr(a),end=" ")
    if i < 3:
        a += 1
    else:
        a -= 1
    print()

