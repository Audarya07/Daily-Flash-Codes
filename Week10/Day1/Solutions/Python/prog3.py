import numpy as np

n = int(input("Length of array:"))
arr = np.array([int(i) for i in input().split()][:n])

print("Max element:",max(arr))
