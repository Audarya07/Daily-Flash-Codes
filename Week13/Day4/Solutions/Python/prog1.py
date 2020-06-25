n = int(input("Enter n:"))

print("Elements in 1st array:",end=" ")
arr1 = [int(i) for i in input().split()][:n]

print("Elements in 2nd array:",end=" ")
arr2 = [int(i) for i in input().split()][:n]

arr3 = arr1 + arr2
print("Array after concatenation->",*arr3)

for i in range(len(arr2)):
    if arr2[i] in arr1:
        arr2[i] = 0

print("Array after replacement:",*(arr1 + arr2))

