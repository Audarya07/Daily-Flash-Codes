n = int(input("Enter value n:"))
nums = [int(i) for i in input().split()][:n]

avg = sum(nums)/n
print("Average of numbers:",round(avg,2))
part = 0
for i in nums:
    part += (i-avg)**2

var = part/n
print("Variance of numbers:",round(var,2))

std_dev = var**0.5
print("Standard deviation:",round(std_dev,2))
