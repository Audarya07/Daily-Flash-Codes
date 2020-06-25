print("------Menu-----\n1)Binary\n2)Hexadecimal\n3)Octal")

num = int(input("\nEnter number:"))
length = len(str(num))
choice = int(input("Enter choice: "))

def converter(num,length,choice):
    while num:
        rem = num//10**(length-1)
        num%=10**(length-1)
        length-=1
        if choice == 1:
            print("Binary of",rem,"=",str(bin(rem))[2:])
        elif choice == 2:
            print("Hexadecimal of",rem,"=",str(hex(rem))[2:])
        elif choice == 3:
            print("Octal of",rem,"=",str(oct(rem))[2:])

converter(num,length,choice)
