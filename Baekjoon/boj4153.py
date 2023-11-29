while True:
    n = list(map(int, input().split()))

    if sum(n) == 0:
        break

    z = max(n)
    n.remove(z)

    if n[0]**2 + n[1]**2 == z**2:
        print('right')
    else:
        print('wrong')