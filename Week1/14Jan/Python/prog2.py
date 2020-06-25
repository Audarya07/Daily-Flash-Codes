a = input()
x = a.casefold()

if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
    print(a + " is a Vowel")
else:
    print(a + " is a Consonant")
