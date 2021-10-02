num = []

for i in range(2, 10000):
    cnt = 0

    for p in range(2, int(i**0.5)+1):
        if i % p == 0:
            cnt += 1
            break

    if cnt == 0:
        num.append(i)

t = int(input())

for i in range(t):
    n = int(input())
    a = n//2
    b = a

    while a > 0:
        if a in num and b in num:
            print(a, b)
            break
        else:
            a -= 1
            b += 1