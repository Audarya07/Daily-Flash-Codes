n = int(input("Enter value n:"))
print("Enter the numbers:",end=" ")
nums = [int(i) for i in input().split()][:n]

print("Choose operation:\n1. Calculate average\n2.Calculate variance\n3.Calculate standard deviation")

conti = "y"

part = 0
for i in nums:
    part += (i-(sum(nums)/n))**2

while conti == "y":
    choice = int(input("Enter choice:"))

    if choice == 1:
        avg = sum(nums)/n
        print("Average of numbers:",round(avg,2))


    elif choice == 2:
        var = part/n
        print("Variance of numbers:",round(var,2))
        

    elif choice == 3:
        std_dev = (part/n)**0.5
        print("Standard deviation:",round(std_dev,2))
        
    else:
        conti = input("Do u want to continue(y/n):")
