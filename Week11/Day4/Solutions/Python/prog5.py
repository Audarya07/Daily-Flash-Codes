length = float(input("Length of pendulum:"))
period = float(input("Enter period of pendulum:"))

g = (4*3.142*3.142*length)/(period**2)

print("Period of pendulum:",round(g,4),"m/s^2")


