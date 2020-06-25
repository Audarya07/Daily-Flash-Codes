print("Enter point A(x1,y1)=",end=" ")
a = [int(x) for x in input().split()]
print("Enter point B(x2,y2)=",end=" ")
b = [int(x) for x in input().split()]

def midpoint(a,b):
    x = (a[0]+b[0])/2
    y = (a[1]+b[1])/2
    return (x,y)

print("Midpoint of line AB=",midpoint(a,b))
