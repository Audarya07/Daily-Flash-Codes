list1 = []
while True:
    num = int(input())
    val = num
    sum = 0
    while val:
        rem = val%10
        sum += rem**3
        val//=10
    if sum == num: 
        print("Output:",*list1)
        print("Terminating!!")
        break
    else:
        list1.append(num)
