num = int(input())
s = set()
while num:
    rem = num%10
    num//=10
    s.add(rem)

print("Second minimum digit is = ",list(s)[1])
