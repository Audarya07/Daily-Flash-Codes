
matrix = []
for i in range(3):
    matrix.append([])
for i in range(3):
    for j in range(3):
        matrix[i].append(int(input()))


for i in range(3):
    for j in range(3):
        x = (matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1]))
        y = (matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0]))        
        z = (matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0]))


det = x-y+z

print("Determinant:",det)

