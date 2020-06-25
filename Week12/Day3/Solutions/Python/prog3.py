import numpy as np

rows = int(input("Enter number of rows:"))
cols = int(input("Enter number of columns:"))

print("Enter elements:")

elements = [int(i) for i in input().split()]

matrix = np.array(elements).reshape(rows,cols)
sum = 0
max_odd = 0
for row in matrix:
    for val in row:
        if val % 2 == 0:
            sum += val
        if val % 2 != 0 and val > max_odd:
            max_odd = val

print("Output:",sum*max_odd)


