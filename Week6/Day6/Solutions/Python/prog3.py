num = int(input())
val=num
rem=0

while num:
    rem = rem*10 + (num%10)
    num//=10
if rem==val:
    print(val,"is Palindrome number")
else:
    print(val,"is NOT palidrome number")
