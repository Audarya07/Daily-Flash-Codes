print("Enter point A(x1,y1)=",end=" ")
a = [int(x) for x in input().split()]
print("Enter point B(x2,y2)=",end=" ")
b = [int(x) for x in input().split()]

slope = (b[1]-a[1])/(b[0]-a[0])

print("Slope of line AB = ",round(slope,2))
