n = int(input("Enter n:"))
r = int(input("Enter r:"))

def fact(num):
    fact = 1
    for i in range(num,0,-1):
        fact *= i
    return fact

per = fact(n) / fact(n-r)

print("To pick",r,"items from a set of",n,"items, there are",int(per),"possible ways")

