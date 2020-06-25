num = int(input("Number: "))
x = int(input("Digit to check frequency: "))
val = num
cnt=0

while num:
    rem = num%10
    num//=10
    if rem==x:
        cnt+=1
print("Frequency of",x,"in the number",val,"is",cnt)
