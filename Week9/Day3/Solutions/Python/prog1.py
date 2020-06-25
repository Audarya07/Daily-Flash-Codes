num = int(input("Enter length os series:"))

mult = 1
for i in range(1,num+1):
    mult *= (i+i)
print("The multiplication of series of length",num,"=",mult)
