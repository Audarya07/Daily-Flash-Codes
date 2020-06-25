print("Point A(x1,y1) = ",end=" ")
a = [int(x) for x in input().split()]

print("Point B(x2,y2) = ",end=" ")
b = [int(x) for x in input().split()]

dist = ((b[0]-a[0])**2 + (b[1]-a[1])**2)**0.5

print("Distance is = ",dist)

