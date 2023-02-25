# 프로그래머스 42840: 모의고사

def solution(answers):
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    cnt = [0, 0, 0]
    
    for i, j in enumerate(answers): # enumerate -> (인덱스, 원소) 튜플 생성
        if a[i%5] == j:
            cnt[0] += 1
        if b[i%8] == j:
            cnt[1] += 1
        if c[i%10] == j:
            cnt[2] += 1
            
    answer = []
    max_value = max(cnt)
    for i in range(0, 3):
        if cnt[i] == max_value:
            answer.append(i+1)
        
    return answer