n = int(input())

val = n
cnt=0
while(n):
    rem = n%10
    n//=10
    if rem%2!=0:
        cnt+=1
print("The number",val,"has",cnt,"odd digits")
