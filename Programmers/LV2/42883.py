# 프로그래머스 42883: 큰 수 만들기 (수정중 - tc10 시간 초과)

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