a = int(input("First number ="))
b = int(input("Second number ="))

sum1 = 0
sum2 = 0

for i in range(1,a):
    if a%i == 0:
        sum1 += i
for i in range(1,b):
    if b%i == 0:
        sum2 += i

if sum1 == b and sum2 == a:
    print("Numbers are Amicable!!")
else:
    print("Not amicable")
