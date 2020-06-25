from numpy import array
n = int(input("Enter length of array:"))
arr = array([int(i) for i in input().split()][:n])

ans = []
for i in arr:
    if i%2 == 0:
        ans.append(i**2)
    else:
        ans.append(i**3)
print("Array after operation:",*ans)
