num = int(input())
val = num
l = []

while num:
    rem = num%10
    num //= 10
    l.append(rem)
print("Min digit from",val,"is",min(l))
