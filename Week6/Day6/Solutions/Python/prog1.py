num = int(input())
val=num
sum=0
while num:
    rem = num%10
    num//=10
    sum+=rem
if val%sum==0:
    print(val,"is Harshad number")
else:
    print(val,"is NOT Harshad number")
