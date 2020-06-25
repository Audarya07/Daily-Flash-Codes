string = input("Enter string:")

dict1 = {i:len(i) for i in string.split()}

for i,j in dict1.items():
    if j == min(dict1.values()):
        print("Word of minimum length:",i)
