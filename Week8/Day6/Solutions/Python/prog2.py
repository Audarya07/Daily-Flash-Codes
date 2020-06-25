num = input()
num = list(map(int,num))
for i,val  in enumerate(num):
    if val == 1:
        num[i] = max(num)
num = list(map(str,num))
print("Output = ","".join(num))

    
        
