import sys
t = int(sys.stdin.readline())

for i in range(t):
    n = int(sys.stdin.readline())
    p = []

    for j in range(n):
        r1, r2 = map(int, sys.stdin.readline().split())
        p.append([r1, r2])

    p.sort()
    k = n + 1
    cnt = 0

    for j in range(n):
        if p[j][1] < k:
            cnt += 1
            k = p[j][1]

    print(cnt)