import numpy as np

r = int(input("Enter no. of rows:"))
c = int(input("Enter no. of cols:"))

print("Enter elements:")

elements = [int(i) for i in input().split()]

matrix = np.array(elements).reshape(r, c)

print(matrix.transpose())

