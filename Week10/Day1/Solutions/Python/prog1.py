n = int(input("Enter length of series:"))
ans = 0

for i in range(1,n+1):
    ans += i/(i*(i+1))**0.5

print("The addition of series:",round(ans,2))
