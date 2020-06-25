num = int(input())
val = num
primes = []
while num:
    rem = num%10
    num//=10
    cnt = 0
    for i in range(1,rem+1):
        if rem%i==0:
            cnt+=1
    if cnt==2:
        primes.append(rem)
print("Prime digits in the number",val,"are",*primes[::-1])
