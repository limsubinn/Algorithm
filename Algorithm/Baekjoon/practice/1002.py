t = int(input())

for i in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    rp = r1 + r2
    rm = abs(r1 - r2)

    if d == 0:
        if rm == d:
            print(-1)
        else:
            print(0)
    else:
        if rp > d:
            if rm < d:
                print(2)
            elif rm > d:
                print(0)
            else:
                print(1)
        elif rp < d:
            print(0)
        else:
            print(1)