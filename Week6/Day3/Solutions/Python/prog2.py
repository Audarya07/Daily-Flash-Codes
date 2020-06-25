num = int(input())
length = len(str(num))
while num:
    rem = num//10**(length-1)
    num %= 10**(length-1)
    length -= 1
    ans = ""
    if rem==1:
        print("Binary of",rem,"= 000"+str(rem))
    val=rem
    if rem>1 and rem<=3:
        while rem:
            ans += str(rem%2)
            rem //= 2
        print("Binary of",val,"= 00"+ans[::-1])
    elif rem>3 and rem<=7:
        while rem:
            ans += str(rem%2)
            rem //= 2
        print("Binary of",val,"= 0"+ans[::-1])

    else:
        while rem:
            ans += str(rem%2)
            rem //= 2
        print("Binary of",val,"=",ans[::-1])
