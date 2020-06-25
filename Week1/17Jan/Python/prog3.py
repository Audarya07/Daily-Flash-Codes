age = int(input("Enter age = "))
gen = input("Enter gender(M or F) = ")
mstatus = input("Enter marital status(Y or N) = ")

if gen == "F":
    print("Work only in urban areas")
elif gen == "M" and (age >=20 and age <=40):
    print("Work anywhere")
elif gen == "M" and (age >40 and age <=60):
    print("Work in urban areas only")
else:
    print("ERROR")
