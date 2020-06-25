num = 0

while num >= 0:
    num = int(input())
    if num < 0:
        print("You entered negative number!!")
    else:
        square = num ** 2
        print("Square:",square)
