num = input("Enter number:")
re_from = input("Enter digit from number to replace:")
re_to = input("Enter digit to replace with:")

if re_from not in num or re_to not in num:
    print("Invalid entry!!")
if re_from in num and re_to in num:
    num = num.replace(re_from,re_to)

print("Output:",num)
