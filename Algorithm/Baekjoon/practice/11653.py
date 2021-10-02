n = int(input())
k = 2

while k <= n:
    if n % k != 0:
        k += 1
    else:
        n //= k
        print(k)