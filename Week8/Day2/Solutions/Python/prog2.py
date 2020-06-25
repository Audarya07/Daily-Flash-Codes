alpha = 65
cnt = 0
while alpha != 91:
    al = input()
    if al == chr(alpha + cnt):
        cnt += 1
    else:
        break
