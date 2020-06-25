s1 = int(input("Side 1 = "))
s2 = int(input("Side 2 = "))
h = int(input("Hypotenuse = "))

if h == (s1**2 + s2**2)**0.5:
    print("Triangle satisfies the Pythagoras Theorem")
else:
    print("Triangle does not satisfy the Pythagoras Theorem")
