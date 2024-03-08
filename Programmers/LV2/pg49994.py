# 프로그래머스 49994: 방문 길이

def solution(dirs):
    # 방문 좌표
    dx = {"U": -1, "L": 0, "R": 0, "D": 1}
    dy = {"U": 0, "L": -1, "R": 1, "D": 0}

    # 연결을 표시할 그래프
    graph = [[[] for _ in range(11)] for _ in range(11)]

    # 초기값
    x, y = 5, 5
    answer = 0

    for dir in list(dirs):
        mx = x + dx[dir]
        my = y + dy[dir]

        # 범위를 벗어나는 경우
        if mx < 0 or mx >= 11 or my < 0 or my >= 11:
            continue

        # 캐릭터가 처음 걸어보는 길인 경우
        if not ([x, y] in graph[mx][my] \
                or [mx, my] in graph[x][y]):
            graph[x][y].append([mx, my])
            answer += 1

        x, y = mx, my

    return answer