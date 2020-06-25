s = "HELLO"

for i in range(9):
    for j in range(len(s)):
        if i+j < 4 or i-j > 4:
            print(" ",end="    ")
        else:
            print(s[j],end="    ")
    print()
