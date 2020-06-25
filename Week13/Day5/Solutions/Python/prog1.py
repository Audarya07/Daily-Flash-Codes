s1 = input("Enter string 1:")
s2 = input("Enter string 2:")

i, j = 0, 0

while s1:
    if s1[i] == s2[j]:
        i+=1
        j+=1
    else:
        print("Difference:",ord(s1[i]) - ord(s2[j]))
        break
