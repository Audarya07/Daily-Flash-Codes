n = int(input("Enter length of series:"))
mult = 1

for i in range(1,n+1):
    mult *= (i**2)

print("The multiplication of Series of length",n,"=",mult)
