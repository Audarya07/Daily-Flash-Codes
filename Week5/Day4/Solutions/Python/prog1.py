num = int(input())
val=num
sum=0
while num:
    rem = num%10
    num //= 10
    fact = 1
    for i in range(1,rem+1):
        fact*=i
    sum+=fact
if sum==val:
    print(val,"is Strong number")
else:
    print(val,"is NOT Strong number!!")
