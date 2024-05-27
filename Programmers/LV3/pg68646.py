# 프로그래머스 68646: 풍선 터트리기

def solution(a):
    center = a.index(min(a))  # 최솟값 인덱스
    answer = 1

    m = float('INF')
    for i in range(center):
        if a[i] < m:
            answer += 1
            m = a[i]

    m = float('INF')
    for i in range(len(a) - 1, center, -1):
        if a[i] < m:
            answer += 1
            m = a[i]

    return answer