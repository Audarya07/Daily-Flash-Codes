import numpy as np
n = int(input("Enter length of array:"))
arr = np.array([int(i) for i in input().split()][:n])

ans = [i**2 for i in arr if i%2 != 0]

print("Output:",*ans)
