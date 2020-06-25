import numpy as np

n = int(input("Enter length of array:"))
arr = np.array([int(i) for i in input().split()][:n])
print("Minimum element of array:",min(arr))
