# 프로그래머스 86491: 최소직사각형

def solution(sizes):
    w = 0
    h = 0
    for i, j in sizes:
        w = max(w, max(i, j))
        h = max(h, min(i, j))
    return w * h