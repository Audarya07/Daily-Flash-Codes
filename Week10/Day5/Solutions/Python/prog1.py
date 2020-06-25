n = int(input("Enter length of series:"))
x = int(input("X:"))
y = int(input("Y:"))

ans = 0
for i in range(1,n+1):
    if i%2 == 1:
        ans += i/(x + y)**x
    elif i%2 == 0:
        ans += i/(x + y)**y

print("Output:",ans)
