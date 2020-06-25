print("********MENU********\n1.Calculate distances of each side of triangle\n2.Calculate perimeter of triangle\n3.Area of triangle\n4.Radius of In-circle\n5.Centre of In-circle")

choice = int(input("Enter choice:"))

print("A(x1,y1)=",end=" ")
a = [int(x) for x in input().split()][:2]

print("B(x2,y2)=",end=" ")
b = [int(x) for x in input().split()][:2]

print("C(x3,y3)=",end=" ")
c = [int(x) for x in input().split()][:2]

distAB = ((b[0]-a[0])**2 + (b[1]-a[1])**2)**0.5
distBC = ((c[0]-b[0])**2 + (c[1]-b[1])**2)**0.5
distAC = ((c[0]-a[0])**2 + (c[1]-a[1])**2)**0.5

if choice == 1:
    print("Distance AB = ",round(distAB,2))
    print("Distance BC = ",round(distBC,2))
    print("Distance AC = ",round(distAC,2))

elif choice == 2:
    p = round(distAB + distBC + distAC,2)
    print("Perimeter of trangle:",p)

elif choice == 3:
    sp = round(distAB + distBC + distAC,2)/2
    area = (sp*(sp - distAB)*(sp - distBC)*(sp - distAC))**0.5
    print("Area of triangle:",round(area,2))

elif choice == 4:
    sp = round(distAB + distBC + distAC,2)/2
    area = (sp*(sp - distAB)*(sp - distBC)*(sp - distAC))**0.5
    radius = area/sp
    print("Radius of in-circle:",round(radius,2))

elif choice == 5:
    X = ((distBC * a[0]) + (distAC * b[0]) + (distAB * c[0])) / p
    Y = ((distBC * a[1]) + (distAC * b[1]) + (distAB * c[1])) / p
    print("Centre of In-Circle(x,y):",(round(X,2),round(Y,2)))
