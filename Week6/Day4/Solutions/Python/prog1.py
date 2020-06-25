import math 

angle = int(input("Angle: "))
radius = int(input("Radius: "))
x = radius*math.cos(math.radians(angle))
y = radius*math.sin(math.radians(angle))

print("X = ",round(x,2),"and","Y = ",round(y,2))
