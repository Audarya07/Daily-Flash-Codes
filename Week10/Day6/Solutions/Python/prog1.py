n = int(input("Enter length of series:"))

x = int(input("X:"))
y = int(input("Y:"))

ans = 0
for i in range(1,n+1):
    ans += (x+y)**i

print("Output:",ans)
