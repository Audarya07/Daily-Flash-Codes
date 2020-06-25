import numpy as np

num = input("Enter number:")

array = np.array([i for i in num])
print("Number stored in array:",*array)
