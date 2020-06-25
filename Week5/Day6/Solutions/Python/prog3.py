val = input()
num = int(val)
length = len(val)
while num:
    rem=num//10**(length-1)
    num%=10**(length-1)
    length-=1
    print("The square of",rem,"is",rem**2)
