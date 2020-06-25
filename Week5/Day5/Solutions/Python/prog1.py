num = int(input())

for val in range(1,num):
    x=val
    sum=0
    while val:
        rem=val%10
        val//=10
        fact=1
        for i in range(1,rem+1):
            fact*=i
        sum+=fact
    if sum==x:
        print(x,end=" ")
print()
