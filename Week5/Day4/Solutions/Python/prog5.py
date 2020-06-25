num = int(input())
ecnt = 0
ocnt = 0
val = num
while num:
    rem = num%10
    num //= 10
    if rem%2==0:
        ecnt += 1
    else:
        ocnt += 1

print("The number",val,"contains",ocnt,"odd digits","and",ecnt,"even digits")
