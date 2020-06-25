p = int(input("Physics score = "))
c = int(input("Chemistry score = "))
b = int(input("Biology score = "))
m = int(input("Maths score = "))
cs = int(input("CS score = "))

per = int((p+c+b+m+cs)/500*100)

if per >= 90:
    print("Grade A")
elif per >= 80:
    print("Grade B")
elif per >= 70:
    print("Grade C")
elif per >= 60:
    print("Grade D")
elif per >= 40:
    print("Grade E")
else:
    print("Grade F")
