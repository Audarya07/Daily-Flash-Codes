num = int(input())
val = num
s = set()
while num:
    rem = num%10
    num //= 10
    s.add(rem)

print("Second max digit from number",val,"is",list(s)[-2])
