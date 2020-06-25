n = int(input("Enter length of series:"))
ans = 1
sum = 0
list1 = []
for i in range(1,n+1):
    sum += i
    list1.append(sum)
for i in list1:
    ans *= i
print("Multiplication of series:",ans)
