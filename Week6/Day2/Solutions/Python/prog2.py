num = int(input())
sum = 0
cnt=0
while num:
    rem = num%10
    num//=10
    cnt+=1
    sum+=rem
print("Sum of digits:",sum)
print("Average of sum of digits:",sum//cnt)
