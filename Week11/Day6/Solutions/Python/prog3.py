from numpy import array

n = int(input("Enter length of array:"))
print("Enter elements in first array:",end=" ")
arr1 = array([int(i) for i in input().split()][:n])
print("Enter elements in second array:",end=" ")
arr2 = array([int(i) for i in input().split()][:n])

arr1,arr2 = arr2,arr1

print("Array 1=",*arr1)
print("Array 2=",*arr2)
