n = int(input())
sum1=0
list1 = []
for i in range(n):
    sum1+=10**i
    list1.append(sum1)
print("The sum is",sum(list1))
