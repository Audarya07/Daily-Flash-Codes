num = 0
while num >= 0:
    num = int(input())
    i = 1
    sum = 0
    while i < num:
        if num % i == 0:
            sum += i
        i += 1
    if sum == num:
        print("output =",num)
else:
    print("Terminating!!")
    
