num = input()
sum=0
for i in range(len(num)):
    sum+=int(num[i])**(i+1)

if str(sum) == num:
    print(num,"is a Disarium Number")
else:
    print(num,"is not a Disarium Number")
