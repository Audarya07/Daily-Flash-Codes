print("Point A(x1,y1) = ",end=" ")
a = [int(x) for x in input().split()][:2]

print("Point B(x2,y2) = ",end=" ")
b = [int(x) for x in input().split()][:2]

print("Point c(x3,y3) = ",end=" ")
c = [int(x) for x in input().split()][:2]

distAB = ((b[0]-a[0])**2 + (b[1]-a[1])**2)**0.5
print("Distance AB = ",round(distAB,2))

distBC = ((c[0]-b[0])**2 + (c[1]-b[1])**2)**0.5
print("Distance BC = ",round(distBC,2))

distAC = ((c[0]-a[0])**2 + (c[1]-a[1])**2)**0.5
print("Distance AC = ",round(distAC,2))
