num = int(input())
l = []
while num:
    rem = num%10
    num//=10
    l.append(rem)
rev = l[::-1]
for i in range(len(rev)):
    print("Hexadecimal of",rev[i],"is",rev[i])

