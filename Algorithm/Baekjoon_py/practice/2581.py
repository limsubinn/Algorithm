m = int(input())
n = int(input())
res = []
cnt = 0

for i in range(m,n+1):
    cnt = 0
    k = 2

    if i == 1:
        cnt += 1

    while i > k:
        if i % k == 0:
            cnt += 1
            break

        k += 1

    if cnt == 0:
        res.append(i)

if res:
    print(sum(res))
    print(min(res))
else:
    print(-1)




m = int(input())
n = int(input())
res = []
cnt = 0

for i in range(m,n+1):
    cnt = 0
    k = 2

    if i == 1:
        cnt += 1

    while i > k:
        if i % k == 0:
            cnt += 1
            break

        k += 1

    if cnt == 0:
        res.append(i)

if res:
    print(sum(res))
    print(min(res))
else:
    print(-1)