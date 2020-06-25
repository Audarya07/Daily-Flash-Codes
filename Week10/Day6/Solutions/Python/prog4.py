string = input("Enter a string:")

for i in range(2*len(string)-1):
    for j in range(len(string)):
        if j > i or i+j >= 2*len(string)-1:
            print(" ",end=" ")
        else:
            print(string[j],end=" ")
    print()
