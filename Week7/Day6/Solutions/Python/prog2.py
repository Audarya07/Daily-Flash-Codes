num = input()

print("value at ones place:",num[-1])
print("value at tens place:",num[-2])
print("value at hundreds place:",num[-3])
if len(num)==4:
    print("value at thousands place:",num[-4])
