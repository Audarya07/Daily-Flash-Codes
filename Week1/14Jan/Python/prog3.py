x = input()

if (x >= 'a' and x <= 'z') or (x >= 'A' and x <= 'Z'): 
    print(x, "is an Alphabet") 
elif x >= '0' and x <= '9':
    print(x,"is a Digit")
else:
    print(x,"is a Special Character")
