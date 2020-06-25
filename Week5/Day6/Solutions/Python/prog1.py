num = int(input())
print("The prime digits are:")
while(num):
    rem = num%10
    num//=10
    cnt=0
    for i in range(1,rem+1):
        if rem%i==0:
            cnt+=1
    if cnt==2:
        print(rem,end=" ")
print()
