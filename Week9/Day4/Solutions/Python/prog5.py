n = int(input("Enter value N:"))
print("Enter values:",end=" ")
num = [int(x) for x in input().split()][:n]
avg = sum(num)/n

print("Average of numbers:",round(avg,2))
