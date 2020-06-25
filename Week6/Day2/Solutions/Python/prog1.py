start = int(input("Starting element:"))
num = int(input("Number of elements:"))
cd = int(input("Common difference:"))

sum1 = start
for i in range(1,num+1):
    print(sum1,end=" ")
    sum1 += cd
print()

