for num in range(1,61):
    if (int(num)**2) % 10 == int(num) or (int(num)**2)% 100 == int(num):
        print(num)

