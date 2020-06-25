x = int(input())
for val in range(1,x+1):
    sum=0
    for i in range(1,val):
        if val%i==0:
            sum+=i
    if sum==val:
        print(val,end=" ")
print()
