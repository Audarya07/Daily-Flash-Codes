string = input("Enter string:")
vowels = ['a', 'e', 'i', 'o', 'u']
dict1 = {i:string.count(i) for i in vowels}
for k,v in dict1.items():
    print(k,"=",v)

