# 프로그래머스 12980: 점프와 순간 이동

def solution(n):
    answer = 1
    while n > 1:
        answer += n % 2
        n //= 2
    return answer