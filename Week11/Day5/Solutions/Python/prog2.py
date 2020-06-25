string = input("Enter string:")
vowels = ['a', 'e', 'i', 'o', 'u']
cnt = 0
for i in string:
    if i in vowels:
        cnt += 1

print("Vowels occured",cnt,"times in the string")
