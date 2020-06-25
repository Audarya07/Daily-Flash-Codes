num = int(input())
l = []
while num:
    rem = num%10
    num//=10
    l.append(rem)

for i in l[::-1]:
    print("Octal of",i,"=",str(oct(i))[2:])
