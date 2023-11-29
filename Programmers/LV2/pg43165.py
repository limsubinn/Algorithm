# 프로그래머스 43165: 타겟 넘버

from collections import deque

def solution(numbers, target):
    answer = 0
    
    queue = deque()
    queue.append([deque(numbers), 0]) # [남은 숫자, 계산값]
    
    while queue:
        number, res = queue.popleft()
        if number:
            num = number.copy()
            n = num.popleft()
            plus = res + n
            minus = res - n
            queue.append([num, plus])
            queue.append([num, minus])
        else:
            if res == target:
                answer += 1
                
    return answer