# 프로그래머스 131130: 혼자 놀기의 달인

def solution(cards):
    open = []
    answer = [1]
    size, i, j = 0, 0, 0
    
    while True:
        open.append(cards[i])
        size += 1
        i = cards[i] - 1
        
        if cards[i] in open:
            answer[j] *= size
            if len(open) == len(cards):
                break
            temp = set(cards) - set(open)
            i = min(temp) - 1
            j += 1
            answer.append(1)
            size = 0

    if len(answer) < 2:
        return 0
    
    answer.sort(reverse = True)
    
    return answer[0] * answer[1]