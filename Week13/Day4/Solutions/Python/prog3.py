import numpy as np

r = int(input("Enter no. of rows:"))
c = int(input("Enter no. of cols:"))

print("Enter elements:")

elements = [int(i) for i in input().split()]

matrix = np.array(elements).reshape(r, c)
matrix1 = np.array(matrix)

final_arr = matrix.sum(axis=1)

matrix1[0] = 2*matrix[0] + 3*matrix[1]
matrix1[1] = 2*matrix[1] - matrix[2]
matrix1[2] = 4*matrix[2]

print("Output:")
print(matrix1)


