n = int(input("Enter value on n = "))
list1 = [str(9)*i for i in range(1,n+1)]
for i in range(len(list1)):
    list1[i]=int(list1[i])

print("Sum of series=",sum(list1))
