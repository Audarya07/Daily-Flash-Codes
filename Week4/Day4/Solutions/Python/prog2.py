num = int(input("Enter decimal number:"))
ans = ""
while num:
    rem = num%2
    num//=2
    ans += str(rem)
print("Binary number:",ans[::-1])
