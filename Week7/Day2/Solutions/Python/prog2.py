num = int(input("Enter number: "))
if num < 200 or num > 600:
    print("Please enter valid number")
else:
    print("Square root of",num,"is",int(num**0.5))
