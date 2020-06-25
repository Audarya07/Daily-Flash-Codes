import numpy as np

num = int(input())
list1 = []
while num:
    rem = num%10
    num//=10
    list1.append(rem)
arr = np.array(list1)
print("Number stored in array:",*arr)
