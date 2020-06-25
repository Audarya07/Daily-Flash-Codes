num = int(input("Decimal number:"))
ans = ""
while num:
    rem = num%16
    num//=16
    if rem < 10:
        ans+=str(rem)
    elif rem == 10:
        ans+="A"
    elif rem == 11:
        ans+="B"
    elif rem == 12:
        ans+="C"
    elif rem == 13:
        ans+="D"
    elif rem == 14:
        ans+="E"
    elif rem == 15:
        ans+="F"
print(ans[::-1])
