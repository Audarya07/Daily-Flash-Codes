from numpy import array

n = int(input("Enter n:"))
arr = array([int(i) for i in input().split()][:n])
print("Output:")
for i in arr:
    if str(i) == str(i)[::-1]:
        print(i)

