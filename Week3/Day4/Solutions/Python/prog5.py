print("Enter number 1:")
x1 = int(input("Real part:"))
y1 = int(input("Imaginery part:"))
c1 = complex(x1,y1)
print("\nEnter number 2:")
x2 = int(input("Real part:"))
y2 = int(input("Imaginery part:"))
c2 = complex(x2,y2)

ans = c1+c2
print("Addition of",c1,"and",c2,"is:",ans)
