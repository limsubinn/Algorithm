n = int(input())
num = list(map(int,input().split()))
cnt = 0

for i in num:
    k = 2

    if i == 1:
        cnt += 1

    while i > k:
        if i % k == 0:
            cnt += 1
            break

        k += 1

print(n-cnt)