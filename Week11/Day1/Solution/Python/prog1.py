def fact(num):
    fact = 1
    for i in range(num,0,-1):
        fact *= i
    return fact


n = int(input("Enter length of series:"))
ans = 0

for i in range(1,n+1):
    ans += 1/fact(i)

print("Addition of series:",round(ans,2))
