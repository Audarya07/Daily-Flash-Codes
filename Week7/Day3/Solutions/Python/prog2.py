def sqrt(num):
    temp = num
    for i in range(1,num+1):
        if temp/i == i:
            print("Square root of",num,"is",i)
            return True

for i in range(200,601):
    sqrt(i)

