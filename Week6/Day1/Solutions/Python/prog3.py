num = int(input())

mul = 1
while num:
    rem = num%10
    num //= 10
    if rem%2 == 0:
        mul *= rem
print("Multiplication of even digits:",mul)
