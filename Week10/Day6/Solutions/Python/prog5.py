def prime(num):
    cnt = 0
    for i in range(1,num+1):
        if num % i == 0:
            cnt += 1
    if cnt == 2:
        return 1
    else:
        return 0

sum = 0
i = 0
num = int(input("Enter number:"))
val = num
length = len(str(num))
rem = 0

while i < length:
    rem = num % 10
    num //= 10
    num = rem*(10**(length-1)) + num
    isprime = prime(num)
    sum += isprime
    i += 1

if sum == length:
    print(val,"is circular prime")
else:
    print(val,"is NOT circular prime")
