length = float(input("Length of pendulum:"))

time = 2*(3.142)*(length/9.81)**0.5
freq = 1/time

print("Period of pendulum:",round(time,2),"seconds")
print("Frequency of pendulum:",round(freq,2),"Hz")


