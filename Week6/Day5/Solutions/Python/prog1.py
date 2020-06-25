import math

theta = (int(input("Theta: ")))*(3.142/180)
phi = (int(input("Phi: ")))*(3.142/180)
r = int(input("R: "))

x = r*math.sin(theta)*math.cos(phi)
y = r*math.sin(theta)*math.sin(phi)
z = r*math.cos(theta)

print("X:",round(x,3)," Y:",round(y,3)," Z:",round(z,3))


