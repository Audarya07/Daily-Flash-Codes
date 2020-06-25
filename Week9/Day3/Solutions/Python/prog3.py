ans = []
while True:
    num = int(input())
    val = num
    sum = 0
    while num:
        fact = 1
        i = 1
        rem = num%10
        while i <= rem:
            fact *= i
            i += 1
        sum += fact
        num //= 10
    if sum == val:
        print("Output:",*ans)
        print("Terminating!!")
        break
    else:
        ans.append(val)
