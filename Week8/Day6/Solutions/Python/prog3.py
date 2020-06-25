while True:
    num = input()
    if int(num) < 0:
        print("Terminating!!")
        break
    if not num.startswith("0") and "0" in num:
        print("Output = ",num)

