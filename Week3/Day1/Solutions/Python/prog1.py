x = int(input("Min of series:"))
y = int(input("Max of series:"))

print("Series of even numbers ranging between",x,"and",y,"is:")
for i in range(x,y+1):
    if i%2==0:
        print(i,end=" ")
print()
