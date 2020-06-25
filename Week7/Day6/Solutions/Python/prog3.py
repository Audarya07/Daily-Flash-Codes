num = int(input())
s = set()
while num:
    rem = num%10
    num//=10
    s.add(rem)

print("Minimum digit is = ",list(s)[0])
print("Maximum digit is = ",list(s)[-1])
