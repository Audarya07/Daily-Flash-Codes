from numpy import array
n = int(input("Enter length of array:"))
arr = array([int(i) for i in input().split()][:n])

mult = 1

for i in arr:
    if i%2 != 0:
        mult *= i

print("Multiplication of odd elements:",mult)
