s1 = input("Enter string 1:")
s2 = input("Enter string 2:")

for i in range(len(s1)):
    a = s1[i]
    if a in s2:
        s2 = s2.replace(a, "")

print("Output:",s2)

