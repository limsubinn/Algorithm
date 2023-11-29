t = int(input())

for i in range(t):
    x, y = map(int, input().split())

    d = y - x
    n = 0

    while True:
        if n * (n + 1) >= d:
            break
        n += 1

    if n**2 < d:
        print(n * 2)
    else:
        print(n * 2 - 1)