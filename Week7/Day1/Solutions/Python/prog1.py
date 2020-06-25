for val in range(1,101):
    sum=0
    num = val
    while num:
        rem = num%10
        num//=10
        sum+=rem
    if val%sum==0:
        print(val,end=" ")
print()

