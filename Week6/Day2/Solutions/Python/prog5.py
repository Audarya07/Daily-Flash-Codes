num = int(input())
val=num
ans = []
while num:
    rem = num%10
    num//=10
    if val%rem==0:
        ans.append(rem)

print("The perfect divisor digits from number",val,"are",*reversed(ans))
