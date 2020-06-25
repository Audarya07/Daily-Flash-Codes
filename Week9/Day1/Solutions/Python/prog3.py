list1 = []
while True:
    num = input()
    if num == num[::-1] and len(num) > 1:
        print("Output:",*list1)
        print("Terminating!!")
        break
    else:
        list1.append(num)
