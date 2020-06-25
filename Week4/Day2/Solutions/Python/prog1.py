num = int(input())
list1 = []
for i in range(2,num+1):
    if i not in list1:
        print(i,end=" ")
        for j in range(i*i,num+1,i):
            list1.append(j)
print()

