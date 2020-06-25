l = int(input("Lower bound:"))
u = int(input("Upper bound:"))

for val in range(l,u+1):

    sum=0
    for i in range(len(str(val))):
        sum+=int(str(val)[i])**(i+1)

    if str(sum) == str(val):
        print(val,end=" ")
print()
