# 프로그래머스 118667: 두 큐 합 같게 만들기 (2022 KAKAO TECH INTERNSHIP)

from collections import deque

def solution(queue1, queue2):
    if (sum(queue1) + sum(queue2)) % 2 != 0:
        return -1

    length = len(queue1) * 4
    target = (sum(queue1) + sum(queue2)) // 2
    left = sum(queue1)
    
    q1 = deque(queue1)
    q2 = deque(queue2)
    answer = 0
    
    while q1 and q2:
        if left < target:
            q = q2.popleft()
            q1.append(q)
            left += q
            answer += 1
        elif left > target:
            q = q1.popleft()
            q2.append(q)
            left -= q
            answer += 1
        else:
            return answer
        
        if answer >= length:
            return -1
        
    return -1