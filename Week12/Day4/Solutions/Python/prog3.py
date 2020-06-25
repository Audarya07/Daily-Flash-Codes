import numpy as np

r = 0
c = 1

while r != c:
    r = int(input("Enter no. of rows:"))
    c = int(input("Enter no. of cols:"))
    if r != c:
        print("Re-enter order of matrix(same order):")

print("Output:")
print(np.identity(r, dtype=int))
