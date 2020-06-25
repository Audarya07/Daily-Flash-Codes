from numpy import array

n = int(input("Enter n:"))
arr = array([int(i) for i in input().split()])

avg = sum(arr)/n
temp = 0
for i in arr:
    temp += (i-avg)**2

var = temp/n
std_dev = (var)**0.5

print("Mean:",round(avg,3))
print("Variance:",round(var,3))
print("Standard deviation:",round(std_dev,3))
