for num in range(1,101):
    sum = 0
    for i in range(1,num):
        if num%i==0:
            sum+=i
    if sum==num:
        continue
    else:
        print(num,end=" ")
print()
