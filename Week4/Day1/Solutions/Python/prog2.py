val = list(input())
for i in range(len(val)):
    val[i] = int(val[i])
val1 = list(reversed(val))
num = 0
for i,val in enumerate(val1):
    num+=val*2**i
print("Decimal number:",num)
l = ""
while num:
    ans = num%16
    num//=16

    if ans<10:
        l+=str(ans)
    if ans==10:
        l+="A"
    if ans==11:
        l+="B"
    if ans==12:
        l+="C"
    if ans==13:
        l+="D"
    if ans==14:
        l+="E"
    if ans==15:
        l+="F"

print("Hexadecimal number:",l[::-1])
