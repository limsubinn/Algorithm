t = int(input())

for _ in range(t):
    n = int(input())
    scores = [list(map(int, input().split())) for _ in range(2)]

    if n > 1:
        # 대각선 더하기
        scores[0][1] += scores[1][0]
        scores[1][1] += scores[0][0]

    for i in range(2, n):
        for j in range(2):
            # 대각선 최댓값 더하기
            scores[j][i] += max(scores[1-j][i-1], scores[1-j][i-2])

    print(max(scores[0][-1], scores[1][-1]))