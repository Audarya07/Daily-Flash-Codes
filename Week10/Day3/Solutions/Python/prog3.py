from numpy import array
n = int(input("Enter length of array:"))

arr = array([int(i) for i in input().split()][:n])
print("Array before swapping:",*arr)
arr[0], arr[-1] = arr[-1], arr[0]
print("Array after swapping:",*arr)

