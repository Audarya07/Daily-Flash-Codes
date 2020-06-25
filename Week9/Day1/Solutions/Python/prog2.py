num = input("Enter number:")
digit = input("Enter digit to replace with 1:")

if digit not in num:
    print("Please enter digit present in number!!")
if '1' not in num:
    print("1 not present in number!!")

for i in num:
    if i == '1' and digit in num:
        num = num.replace(i,digit)

print("Output:",num)
