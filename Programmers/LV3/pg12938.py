# 프로그래머스 12938: 최고의 집합

def solution(n, s):
    if n > s: # 최고의 집합이 존재하지 않는 경우
        return [-1]

    answer = []
    while s > 0:
        result = s // n
        if s % n == 0:
            answer += [result] * n
            break
        answer += [result] + [result + 1]
        s -= (2 * result + 1)
        n -= 2
    
    return sorted(answer)