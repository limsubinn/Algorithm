# 프로그래머스 12987: 숫자 게임

from collections import deque

def solution(A, B):
    answer = 0
    A = deque(sorted(A))
    B = deque(sorted(B))

    while A and B:
        a = A.popleft()
        b = B.popleft()

        while a >= b: # a < b가 될 때까지 B의 원소를 꺼낸다.
            if not B:
                return answer
            b = B.popleft()
        answer += 1

    return answer