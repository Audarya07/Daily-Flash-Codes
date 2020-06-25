start,end = [int(x) for x in input().split()]
print("Automorphic numbers between",start,"&",end,"are:")
for i in range(start, end + 1):
    if (i**2) % 10 == i:
        print(i,end=" ")
print()
