string = input("Enter string:")

dict1 = {i:len(i) for i in string.split()}

for i,j in dict1.items():
    if j == max(dict1.values()):
        print("Word of max length:",i)
