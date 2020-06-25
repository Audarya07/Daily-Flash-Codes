while(1):
    num = int(input())
    if num >= 0:
        fact = 1
        i = num
        while num > 0:
            fact *= num
            num -= 1
        print("Factorial = ",fact)
    else:
        break

