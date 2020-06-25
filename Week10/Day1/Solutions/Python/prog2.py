string = input("Input:")
vowels = {"A","E","I","O","U"}

for val in string:
    if val in vowels:
        print(val,":",ord(val))
