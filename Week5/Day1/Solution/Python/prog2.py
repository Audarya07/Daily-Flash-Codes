num = int(input("Enter octal number:"))
ans = []
while(num):
    rem = num%10
    if rem == 0:
        ans.append("000")
    elif rem == 1:
        ans.append("001")
    elif rem == 2:
        ans.append("010")
    elif rem == 3:
        ans.append("011")
    elif rem == 4:
        ans.append("100")
    elif rem == 5:
        ans.append("101")
    elif rem == 6:
        ans.append("110")
    elif rem == 7:
        ans.append("111")
    num//=10
print(*ans[::-1],sep="")
