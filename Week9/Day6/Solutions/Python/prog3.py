import numpy as np
n = int(input("Enter length of array:"))
arr = np.array([int(i) for i in input().split()][:n])

sum1 = sum(arr)
avg = sum1/n

print("Sum of elements of array:",sum1)
print("Average of elements:",avg)
