import numpy as np

rows = int(input("Enter number of rows:"))
cols = int(input("Enter number of columns:"))

print("Enter elements:")

elements = [int(i) for i in input().split()]

matrix = np.array(elements).reshape(rows,cols)

print("Diagonal Elements:",*matrix.diagonal())


