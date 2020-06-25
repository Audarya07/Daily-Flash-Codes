n = int(input("Enter length of series:"))
x,y = input("Enter value of x & y:").split()

ans = 0

for i in range(1,n+1):
    ans += i / (int(x) + int(y))**i

print("Sum of series:",round(ans,2))
