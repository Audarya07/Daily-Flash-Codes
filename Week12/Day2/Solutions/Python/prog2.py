string = input("Enter string:")
vowels = ["a","e","i","o","u"]
print("String contains occurences of 2 consecutive vowels as:",end=" ")
i = 0
j = 1
while j < len(string) :
    if string[i] in vowels  and string[j] in vowels:
        print(string[i]+string[j])
        i+=1
        j+=1
        break
    else:
        i+=1
        j+=1
