n = int(input())

if n <= 2:
    print(1)
else:
    temp = 0
    j = 1
    cnt = 1

    for i in range(1, n//2+2):
        while temp < n and j <= n//2 + 1:
            temp += j
            j += 1
        if temp == n:
            cnt += 1
        temp -= i

    print(cnt)