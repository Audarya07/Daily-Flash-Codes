num = int(input())
print("Perfect divisors of",num,"are:",end=" ")
for i in range(1,num):
    if num%i==0:
        print(i,end=" ")

print()
