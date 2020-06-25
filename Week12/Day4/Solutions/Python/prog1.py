import numpy as np

n = int(input("Enter n:"))
print("Array 1:",end=" ")
arr1 = np.array([int(i) for i in input().split()][:n])
print("Array 2:",end=" ")
arr2 = np.array([int(i) for i in input().split()][:n])
arr3 = abs(np.subtract(arr1, arr2))

print("Output:",*arr3)
