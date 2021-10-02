n = int(input())
res = 0

while True:
    if n % 5 == 0:
        res += n // 5
        break
    else:
        n -= 3
        res += 1

    if n < 0:
        res = -1
        break

print(res)