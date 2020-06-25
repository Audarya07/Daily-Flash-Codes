def check(num):
    checker = 1
    for i in range(2,num//2):
        if num%i==0:
            checker = 0
            break
    return checker

num = int(input())

flag = 0
for i in range(2,num//2):
    if check(i)==1 and check(num-i)==1:
        print(num,"=",i,"+",num-i)
        flag=1
        break
if flag==0:
    print(num,"cannot be expressed as sum of primes")


