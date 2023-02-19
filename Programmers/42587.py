# 프로그래머스 42587: 프린터

def solution(priorities, location):
    answer = 0
    
    while True:
        i = priorities.index(max(priorities))
        priorities = priorities[i:] + priorities[:i]
        
        location -= i
        if (location < 0):
            location += len(priorities)
        i = 0

        priorities[i] = 0
        answer += 1

        if i == location:
            return answer