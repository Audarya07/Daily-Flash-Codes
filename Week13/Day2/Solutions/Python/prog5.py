import numpy as np

m = int(input("Row : "))
n = int(input("Col : "))

print("Enter matrix A:")
a1 = [int(i) for i in input().split()]
mat1 = np.array(a1).reshape(m, n)
print("Matrix A:")
print(mat1)
print("Enter matrix B:")
a2 = [int(i) for i in input().split()]
mat2 = np.array(a2).reshape(m, n)
print("Matrix B:")
print(mat2)
comp =  mat1 == mat2
if comp.all():
    print("Both matrix are equal")
else:
    print("Both matrix NOT equal")
