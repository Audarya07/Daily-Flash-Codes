from numpy import array
n = int(input("Enter length of array:"))
arr = array([int(i) for i in input().split()][:n])

ans = 1
for i in arr:
    if i%2 == 0:
        ans *= i

print("Multipliction of even elements:",ans)

