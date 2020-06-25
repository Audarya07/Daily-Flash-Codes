num = int(input())
val=num
print("The quotient of divisions are: ")
length = len(str(val))
while num:
    rem = num//(10**(length-1))
    num %= (10**(length-1))
    length -= 1
    print(val,"/",rem,"=",val//rem)


