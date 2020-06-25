string = "HOME"

for i in range(7):
    for j in range(4):
        if j > i or i+j > 6:
            print(" ",end=" ")
        else:
            print(string[j],end=" ")
    print()
