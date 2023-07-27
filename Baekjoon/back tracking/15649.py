def sol():
    if len(result) == m:
        print(*result)
        return

    for i in range(1, n+1):
        if visited[i]:
            continue

        visited[i] = True
        result.append(i)

        sol()

        visited[i] = False
        result.pop()

n, m = map(int, input().split())
result = []
visited = [False] * (n+1)

sol()