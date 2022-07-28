s = list(input())
cnt = 0

for i in s:
    if i>='A' and i<='C':
        cnt += 3
    elif i>='D' and i<='F':
        cnt += 4
    elif i>='G' and i<='I':
        cnt += 5
    elif i>='J' and i<='L':
        cnt += 6
    elif i>='M' and i<='O':
        cnt += 7
    elif i>='P' and i<='S':
        cnt += 8
    elif i>='T' and i<='V':
        cnt += 9
    else:
        cnt += 10

print(cnt)