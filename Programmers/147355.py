# 프로그래머스 147355: 크기가 작은 문자열

def solution(t, p):
    answer = 0
    size = len(p)
    p = int(p)

    for i in range(len(t) - size + 1):
        j = i + size
        if int(t[i:j]) <= p:
            answer += 1

    return answer