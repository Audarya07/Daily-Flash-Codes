print("A(x1,y1) = ",end=" ")
a = [int(x) for x in input().split()]

print("B(x2,y2) = ",end=" ")
b = [int(x) for x in input().split()]

print("C(x3,y3) = ",end=" ")
c = [int(x) for x in input().split()]

ab = ((b[0]-a[0])**2 + (b[1]-a[1])**2)**0.5
print("Length AB = ",round(ab,2))

bc = ((c[0]-b[0])**2 + (c[1]-b[1])**2)**0.5
print("Length BC = ",round(bc,2))

ac = ((c[0]-a[0])**2 + (c[1]-a[1])**2)**0.5
print("Length AC = ",round(ac,2))


