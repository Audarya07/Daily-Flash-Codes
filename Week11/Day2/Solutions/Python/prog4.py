for i in range(5):
    for j in range(3):
        if i+j < 2 or i-j > 2:
            print("  ",end="   ")
        else:
            print(str(i)+str(j),end="   ")
    print()
