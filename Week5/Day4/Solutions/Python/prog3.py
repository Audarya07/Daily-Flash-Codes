num = int(input())
val = num
sum=0
while num:
    rem = num%10
    num//=10
    sum+=rem
print("The sum digits from number",val,"is",sum)
