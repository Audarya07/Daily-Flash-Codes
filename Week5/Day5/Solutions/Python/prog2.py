num = input("Hexadcimal number:")
decimal = int(num,16)
binary = bin(decimal)
print("Binary number:",binary.strip("0b"))
