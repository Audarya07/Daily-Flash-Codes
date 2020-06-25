num = int(input())
print("Prime factors:")
while num % 2 == 0:
    print("2")
    num //= 2

for i in range(3,int(num**0.5)+1,2):

    while num % i == 0:
        print(i)
        num //= i

if num > 2:
    print(num)
