num = int(input())
val=num
cnt=0
while num:
    rem = num%10
    num//=10
    if rem==1:
        cnt+=1
print("The number",val,"contains",cnt,"Ones")
