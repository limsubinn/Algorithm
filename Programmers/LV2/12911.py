# 프로그래머스 12911: 다음 큰 숫자

def solution(n):
    b = bin(n)[2:]
    cnt = b.count('1')
    answer = n + 1
    
    while True:
        b = bin(answer)[2:]
        
        if b.count('1') == cnt:
            return answer
        
        answer += 1