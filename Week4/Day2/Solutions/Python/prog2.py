num = int(input("Binary Number:"))
val=0
base=1
while num:
    val += (num%10)*base
    num//=10
    base*=2
print("Decimal number:",val)
