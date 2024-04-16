# 프로그래머스 72413: 합승 택시 요금

def floyd(n, fares):
    graph = [[float('INF')] * (n) for _ in range(n)]

    for i in range(n):
        graph[i][i] = 0

    for i, j, k in fares:
        graph[i - 1][j - 1] = k
        graph[j - 1][i - 1] = k

    # 최소 비용 계산
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][k] + graph[k][j] < graph[i][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]

    return graph

def solution(n, s, a, b, fares):
    graph = floyd(n, fares)

    answer = float('INF')
    for i in range(n):
        answer = min(answer, graph[s - 1][i] + graph[i][a - 1] + graph[i][b - 1]) # (s->i) + (i->a) + (i->b)

    return answer