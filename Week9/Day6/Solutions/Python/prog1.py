n = int(input("Enter length of input:"))
ans = 0
for i in range(1,n+1):
    ans += (i**i)*(i-1)

print("The addition of the series:",ans)
