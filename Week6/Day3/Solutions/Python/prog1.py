a = int(input("Starting element: "))
n = int(input("Number of elements: "))
d = int(input("Common difference: "))

sum1 = a

for i in range(n):
    print(sum1,end=" ")
    sum1 += d
    if i!=n-1:
        print("+",end=" ")

print("=",(n//2)*(2*a+(n-1)*d))
