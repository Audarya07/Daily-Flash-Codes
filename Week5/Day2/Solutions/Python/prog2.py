num = int(input("Enter octal number:"))
base = 1
rem = 0
while num:
    rem += (num%10)*base
    num//=10
    base *= 8

print("Decimal number:",rem)



