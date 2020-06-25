num = int(input())
val = num
while num:
    rem = num%10
    num//=10
    sum=0
    for i in range(1,rem):
        if rem%i==0:
            sum+=i
    if sum==rem:
        print(rem,"is perfect number")
    else:
        print(rem,"is not perfect number")
