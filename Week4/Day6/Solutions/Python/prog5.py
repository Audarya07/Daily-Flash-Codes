from numpy import array

arr = array([int(i) for i in input().split()])
print("Output:",*arr[::-1])
