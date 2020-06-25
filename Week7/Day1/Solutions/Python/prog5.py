num = input("Enter number: ")
d = {}

for i in num:
    if i not in d:
        d[i] = 1
    else:
        d[i]+=1
for val in d:
    print("Frequency of",val,"is:",d[val])

