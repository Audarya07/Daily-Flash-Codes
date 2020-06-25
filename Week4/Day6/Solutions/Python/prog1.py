num = int(input())
div = [int(i) for i in range(1,num) if num%i==0]
if sum(div) > num:
    print(num,"is abundant number")
else:
    print(num,"is NOT abundant number")

