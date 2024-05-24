# 프로그래머스 92344: 파괴되지 않은 건물
# https://tech.kakao.com/posts/488 카카오 해설 참고

def solution(board, skill):
    # 누적합을 구하는데 쓰일 배열
    graph = [[0] * (len(board[0]) + 2) for _ in range(len(board) + 2)]

    for s in skill:
        t, r1, c1, r2, c2, d = s

        # 공격일 경우 부호 반대
        if t == 1:
            d = -d

        # 값 넣기
        for r, c, degree in [(r1, c1, d), (r1, c2 + 1, -d), (r2 + 1, c1, -d), (r2 + 1, c2 + 1, d)]:
            graph[r + 1][c + 1] += degree

    # 누적합 구하기
    for i in range(1, len(graph)):
        for j in range(1, len(graph[0])):
            graph[i][j] += graph[i - 1][j] + graph[i][j - 1] - graph[i - 1][j - 1]

    answer = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            # 내구도 > 0 => 파괴되지 않은 건물
            if board[i][j] + graph[i + 1][j + 1] > 0:
                answer += 1
    return answer