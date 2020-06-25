s1 = input("Enter string 1:")
s2 = input("Enter string 2:")
n = int(input("Enter n characters to check:"))

i, j = 0, 0

if s1[:n] == s2[:n]:
        print("Strings are equal")
else:
    while s1:
        if s1[i] == s2[j]:
            i+=1
            j+=1
        else:
            print("Difference:",ord(s1[i]) - ord(s2[j]))
            break
