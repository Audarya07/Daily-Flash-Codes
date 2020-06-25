print("A(x1,y1)=",end=" ")
a = [int(x) for x in input().split()][:2]

print("B(x2,y2)=",end=" ")
b = [int(x) for x in input().split()][:2]

print("C(x3,y3)=",end=" ")
c = [int(x) for x in input().split()][:2]

distAB = ((b[0]-a[0])**2 + (b[1]-a[1])**2)**0.5
print("Distance AB = ",round(distAB,2))

distBC = ((c[0]-b[0])**2 + (c[1]-b[1])**2)**0.5
print("Distance BC = ",round(distBC,2))

distAC = ((c[0]-a[0])**2 + (c[1]-a[1])**2)**0.5
print("Distance AC = ",round(distAC,2))

p = round(distAB + distBC + distAC,2)
sp = round(distAB + distBC + distAC,2)/2
area = (sp*(sp - distAB)*(sp - distBC)*(sp - distAC))**0.5
radius = area/sp
X = ((distBC * a[0]) + (distAC * b[0]) + (distAB * c[0])) / p
Y = ((distBC * a[1]) + (distAC * b[1]) + (distAB * c[1])) / p

print("Perimeter of triangle:", p)
print("Semi-perimeter of triangle:", sp)
print("Area of triangle:",round(area,2))
print("Radius of incircle:",round(radius,2))
print("Centre of In-Circle(x,y):",(round(X,2),round(Y,2)))
