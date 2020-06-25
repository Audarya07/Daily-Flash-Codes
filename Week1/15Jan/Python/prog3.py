dict1 = {1:'Jan',2:'Feb',3:'March',4:'April',5:'May',6:'June',7:'July',8:'August',9:'September',10:'October',11:'November',12:'December'}

x = int(input())

if x in dict1 and x == 2:
    print(dict1[x],"is a 28 days month")
elif x in dict1 and x  == 8:
    print(dict1[x],"is a 31 days month")
elif x in dict1 and x % 2 == 0 and x > 8:
    print(dict1[x],"is a 31 days month")
elif x in dict1 and x % 2 == 0 and x < 8:
    print(dict1[x],"is a 30 days month")
elif x in dict1 and x % 2 != 0 and x > 8:
    print(dict1[x],"is a 30 days month")
else:
    print(dict1[x],"is a 31 days month")
