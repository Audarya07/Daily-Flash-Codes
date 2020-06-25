vowels = ["a","e","i","o","u"]
string = input("Enter string:")
asci = [ord(i) for i in string]
maxi = max(asci)

for i in string:
    if i in vowels:
        string = string.replace(i,chr(maxi))

print("Output:",string)

