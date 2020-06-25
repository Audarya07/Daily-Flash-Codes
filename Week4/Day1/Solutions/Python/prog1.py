x = int(input())
cnt = 0
for i in range(1,x+1):
    if x%i==0:
        cnt+=1
if cnt==2:
    print(x,"is a prime number")
else:
    print(x,"is not a prime number")
