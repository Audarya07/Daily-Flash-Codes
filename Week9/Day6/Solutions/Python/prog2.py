string = input("Input:")
vowels = ["A","E","I","O","U"]
print("Vowels in entered string:",end=" ")
for val in string:
    if val in vowels:
        print(val,end=" ")
print()
