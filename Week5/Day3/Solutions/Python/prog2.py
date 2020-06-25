num = int(input("Octal number:"))
base = 1
dec=0
while(num):
    dec += (num%10)*base
    num//=10
    base *= 8

ans = ""
while(dec):
    rem = dec%16
    dec //= 16
    if rem<10:
        ans += str(rem)
    if rem>=10:
        ans += chr(rem+55)

print("Hexadecimal:",ans[::-1])
