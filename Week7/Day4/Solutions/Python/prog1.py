start = int(input("Enter lower bound = "))
end = int(input("Enter upper bound = "))

for val in range(start,end+1):
    if str(val) == str(val)[::-1]:
        print(val,end=" ")
print()

