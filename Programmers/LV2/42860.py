# 프로그래머스 42860: 조이스틱

def solution(name):
    answer = 0
    for i in name: # 상하이동 먼저 다 더하기
        answer += min(ord(i) - 65, 91 - ord(i))
    
    temp = [] # 연속된 A의 인덱스를 저장할 리스트
    for i in range(1, len(name)):
        if name[i] == 'A':
            if temp and temp[-1][-1] == i-1:
                temp[-1].append(i)
                continue
            temp.append([i])
    
    res = len(name) - 1 # 기존 방식
    for i in temp:
        # (기존 방식, 앞으로 갔다가 뒤로 돌아가기, 뒤로 갔다가 앞으로 돌아가기)의 최솟값
        res = min(res, 2 * (i[0] - 1) + len(name) - 1 - i[-1], 2 * (len(name) - 1 - i[-1]) + i[0] - 1)
            
    return answer + res