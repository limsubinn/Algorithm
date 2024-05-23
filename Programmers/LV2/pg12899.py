# 프로그래머스 12899: 124 나라의 숫자

def solution(n):
    result = []

    while n > 0:
        res = n % 3
        if res == 0:
            res = 4
            n -= 1
        result.append(res)
        n //= 3

    return ''.join(map(str, result[::-1]))