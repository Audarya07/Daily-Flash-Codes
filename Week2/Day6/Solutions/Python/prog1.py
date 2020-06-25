start = int(input("Min of series:"))
stop = int(input("Max of Series:"))

for odd_num in range(start,stop+1):
    if odd_num%2!=0:
        print(odd_num,end=" ")
print()
