string = input("Enter string:")
sub = input("Enter substring to find:")

if sub in string:
    print("The entered string consists",sub,"as substring")
else:
    print("The entered string does not consist the substring")
