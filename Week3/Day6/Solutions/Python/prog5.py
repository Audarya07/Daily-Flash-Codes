list1 = list(int(x) for x in input().split())
div=None
for i in range(1,min(list1)):
    if list1[0]%i==0 and list1[1]%i==0:
        div=i
print("GCD = ",div)


