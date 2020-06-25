r = int(input("Rows:"))
c = int(input("Cols:"))

print("Enter matrix 1:")
mat1 = [[int(input()) for j in range(c)] for i in range(r)]

print("Enter matrix 2: ")
mat2= [[int(input()) for j in range(c)] for i in range(r)]

mat3 = [[0 for j in range(c)] for i in range(r)]

for i in range(r):
    for j in range(c):
        if mat1[i][j] > mat2[i][j]:
            mat3[i][j] = mat1[i][j] / mat2[i][j]
        else:
            mat3[i][j] = mat2[i][j] / mat1[i][j]

print("Output matrix:")
for i in range(r):
    print(*mat3[i])
