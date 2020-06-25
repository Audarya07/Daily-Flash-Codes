x = int(input("Enter first number:"))
y = int(input("Enter second number:"))
sign = input("Enter sign of operation:")

if sign=='+':
    print("Addition of",x,"&",y,"is",x+y)
elif sign=='-':
    print("Subtraction of",x,"&",y,"is",x-y)
elif sign=='*':
    print("Multiplication of",x,"&",y,"is",x*y)
elif sign=='/':
    print("Division of",x,"&",y,"is",x/y)
elif sign=='//':
    print("Floor Division of",x,"&",y,"is",x//y)
