import numpy as np

n = int(input("Enter n:"))
print("Array 1:",end=" ")
arr1 = np.array([int(i) for i in input().split()][:n])

first = arr1[0]
second = 0
for i in arr1[1:]:
    if i > first:
        second = first
        first = i
    elif second == 0 and second < i:
        second = i

print("Second largest element:",second)
