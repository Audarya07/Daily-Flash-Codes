n = int(input("Enter n:"))
r = int(input("Enter r:"))

def fact(num):
    fact = 1
    for i in range(num,0,-1):
        fact *= i
    return fact

combi = fact(n) / (fact(r) * fact(n-r))
per = fact(n)/(fact(n-r))

print("The number of permutations:",int(per))
print("Rhe number of combinations:",int(combi))
