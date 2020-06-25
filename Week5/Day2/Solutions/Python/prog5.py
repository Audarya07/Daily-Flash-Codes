num = int(input())
val = num
cnt=0
while(num):
    rem = num%10
    num//=10
    if rem%2==0:
        cnt+=1
print(val,"has",cnt,"even digits")
