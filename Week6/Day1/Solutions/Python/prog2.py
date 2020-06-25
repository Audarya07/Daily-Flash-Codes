num = int(input())
rev = 0 
while num:
    rev = (rev*10) + (num%10)
    num //= 10
print("Reverse:",rev)
