x = int(input("Enter binary number:"))
base = 1
dec = 0
while x:
    dec += (x%10)*base
    x//=10
    base*=2

print("Octal number:",str(dec//8)+str(dec%8))


