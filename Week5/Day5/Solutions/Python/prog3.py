num = int(input())
val=num
sum=cnt=0
while num:
    rem = num%10
    num//=10
    sum+=rem
    cnt+=1
print("The average of digits of number",val,"is",sum//cnt)
