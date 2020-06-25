date = input("Enter date(dd/mm/yyyy):")
d,m,y = date.split('/')

d=int(d)
m=int(m)
y=int(y)

month_30 = [4,6,9,11]
month_31 = [1,3,5,7,8,10,12]

if m==2 and d>28:
    print("Date does not exist!!")
elif m in month_30:
    if d>30:
        print("Date does not exist!!")
    else:
        print("Date exists!!")
elif m in month_31:
    if d>31:
        print("Date does not exist!!")
    else:
        print("Date exists!!")
