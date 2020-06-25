num1 = int(input("num1:"))
num2 = int(input("num2:"))

for i in range(num1,num2+1):
    fact = 1
    for j in range(1,i+1):
        fact = fact*j
    print("Factorial of",i,":",fact)
print()
