# 프로그래머스 42883: 큰 수 만들기
# 스택을 이용한 풀이

from collections import deque

def solution(number, k):
    number = deque(number)
    num = []
    
    while number:
        n = number.popleft()
        # 현재 수보다 작은 수 제거
        while num and num[-1] < n: 
            num.pop()
            k -= 1
            # k개의 수를 모두 제거했으면 정답 리턴
            if k == 0: 
                return ''.join(num) + n + ''.join(number)
        num.append(n)
    
    # 맨 마지막 문자열 하나만을 제거할 경우
    return ''.join(num[:-1])

'''
문자열을 이용한 풀이 - tc10 시간 초과

def solution(number, k):
    answer = ''
    cnt = 0
    n = number[:k+1]
    
    while k > cnt:
        answer += max(n)
        i = n.index(max(n))
        cnt += i
        number = number[i+1:]
        n = number[:k-cnt+1]
        
        if len(n) == k-cnt:
            return answer
        
    return answer + number
'''