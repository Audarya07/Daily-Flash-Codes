n = int(input("Enter length of series:"))
mult = 1
for i in range(1,n+1):
    mult *= (i**i)
print("Multiplication of series:",mult)
