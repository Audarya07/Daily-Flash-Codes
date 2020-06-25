num = 4
for i in range(4):
    for j in range(4):
        if i+j<3:
            print("  ",end=" ")
        else:
            print(chr(68-j)+str(i+j),end=" ") 
    print()
