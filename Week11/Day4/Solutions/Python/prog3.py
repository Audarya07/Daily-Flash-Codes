from numpy import array

n = int(input("Enter length of array:"))
arr = array([int(i) for i in input().split()])

print("Array after operation:",*sorted(arr,reverse=True))
