val = input()
num = int(val)
length = len(val)

while num:
    rem=num//10**(length-1)
    num%=10**(length-1)
    length-=1
    fact=1
    for i in range(1,rem+1):
        fact*=i
    print("Factorial of",rem,"is",fact)
print()

