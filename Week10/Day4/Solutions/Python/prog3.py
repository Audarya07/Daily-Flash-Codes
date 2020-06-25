from numpy import array

n = int(input("Enter length of array:"))
arr = array([int(i) for i in input().split()][:n])
print("Array before swapping:",*arr)
arr = arr[::-1]
print("Array after swapping:",*arr)

