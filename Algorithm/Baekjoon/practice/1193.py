x = int(input())
num = 1
cnt = 1

while x>num :
    num += cnt + 1
    cnt += 1

if cnt%2==0 :
    a = cnt
    b = 1

    for i in range(num-x):
        a -= 1
        b += 1
else:
    a = 1
    b = cnt

    for i in range(num-x):
        a += 1
        b -= 1

print('%d/%d'%(a,b))