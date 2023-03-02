# 프로그래머스 92342: 양궁대회 (2022 KAKAO BLIND RECRUITMENT)

from collections import deque 

def solution(n, info):
    answer = []
    res = 1 # 비기는 경우 고려하여 1로 초기화
    queue = deque()
    queue.append([0, [0] * 11]) # [pos, score]
    
    while queue:
        pos, q = queue.pop()
        
        if sum(q) == n or (sum(q) < n and pos == 9): # 10~1점까지 모든 화살을 다 쏜 경우
            if (sum(q)) < n:
                q[10] = n - sum(q) # 0점에 남은 화살 몰아주기

            ryan = 0
            apeach = 0
            for i in range(10): # 점수 계산 (0점은 계산할 필요 X)
                if q[i] > 0:
                    ryan += 10 - i
                elif info[i] > 0:
                    apeach += 10 - i

            if res < ryan-apeach: # 최댓값 갱신
                answer = [q]
                res = ryan - apeach
            elif res == ryan-apeach:
                answer.append(q)

        elif sum(q) < n: # 남은 화살이 존재할 경우
            q1 = q.copy()
            q2 = q.copy()
            
            q1[pos] = 0
            q2[pos] = info[pos] + 1
            pos += 1
            
            queue.append([pos, q1])
            queue.append([pos, q2])

    if answer:
        answer.sort(key = lambda x : x[::-1]) # 원소를 거꾸로 정렬
        return answer[-1]
    
    return [-1]