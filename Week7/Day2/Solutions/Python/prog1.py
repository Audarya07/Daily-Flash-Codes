lbound = int(input("Lower bound: "))
ubound = int(input("Upper bound: "))

for val in range(lbound,ubound+1):
    j=val
    sum=0
    while j:
        rem = j%10
        j //= 10
        sum+=rem
    if val%sum==0:
        print(val,end=" ")
print()
