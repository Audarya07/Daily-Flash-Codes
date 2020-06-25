dict1 = {1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine"}
ans = []
num = int(input())

while num:
    rem = num%10
    num//=10
    if rem in dict1:
        ans.append(dict1[rem])
print(*ans[::-1])
