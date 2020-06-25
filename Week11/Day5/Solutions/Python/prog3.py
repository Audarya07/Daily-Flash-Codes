from numpy import array

n = int(input("Enter length of array:"))
print("Enter elements in first array:",end=" ")
arr1 = array([int(i) for i in input().split()][:n])
print("Enter elements in second array:",end=" ")
arr2 = array([int(i) for i in input().split()][:n])

arr3 = array([(i*j) for i,j in zip(arr1, arr2)])

print("After operation elements in 3rd array:",*arr3)
