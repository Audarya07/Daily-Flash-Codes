import numpy as np

r = int(input("Enter no. of rows:"))
c = int(input("Enter no. of cols:"))

print("Enter elements:")

elements = [int(i) for i in input().split()]

matrix = np.array(elements).reshape(r, c)
matrix1 = np.array(matrix)

print(matrix[:,1])

matrix1[:,0] = 2*matrix[:,2] + matrix[:,1]
matrix1[:,1] = 3*matrix[:,1] - matrix[:,0]
matrix1[:,2] = 3*matrix[:,2]

print("Output:")
print(matrix1)


