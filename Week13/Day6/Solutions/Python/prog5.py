r = int(input("Rows:"))
c = int(input("Cols:"))
l4 = []

print("Enter matrix 1:")
mat1 = [[int(input()) for j in range(c)] for i in range(r)]

print("Enter matrix 2: ")
mat2= [[int(input()) for j in range(c)] for i in range(r)]

for i in range(r):
    l3 = []
    for j in range(c):
        sum = 0
        for k in range(c):
            sum += mat1[i][k] * mat2[k][j]
        l3.append(sum)
    l4.append(l3)

print("Output:")

for i in range(r):
    for j in range(c):
        print(l4[i][j],end=" ")
    print()
print()
