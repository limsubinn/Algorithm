# 프로그래머스 12900: 2 x n 타일링

def solution(n):
    d = [[] for _ in range(n + 1)]
    d[1] = 1
    d[2] = 2
    d[3] = 3

    for i in range(4, n + 1):
        d[i] = (d[i - 1] + d[i - 2]) % 1000000007

    return d[n]