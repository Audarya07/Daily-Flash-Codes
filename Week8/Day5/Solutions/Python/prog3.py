num = 0

while num >= 0:
    num = int(input())
    i = 2
    cnt = 0
    while i <= num//2:
        if num % i == 0:
            cnt += 1
            break
        i+=1
    if cnt == 0 and cnt != 1 and num > 0:
        print("Output =",num)
else:
    print("Terminating!!")
