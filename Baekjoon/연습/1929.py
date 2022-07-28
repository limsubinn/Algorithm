m, n = map(int, input().split())
num = [i for i in range(m,n+1)]

for i in num:
    cnt = 0

    if i == 1:
        cnt += 1

    for p in range(2, int(i**0.5)+1):
        if i % p == 0:
            cnt += 1
            break

    if cnt == 0:
        print(i)