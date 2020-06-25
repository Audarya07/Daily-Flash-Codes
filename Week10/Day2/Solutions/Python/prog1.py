n = int(input("Enter length of series:"))

ans = 0
list1 = [0,30,60,90,120,150,180,210,240,270,300,330,360]
for i in range(n):
    ans+=list1[i]
print("Output:",(ans*3.14)/180)
