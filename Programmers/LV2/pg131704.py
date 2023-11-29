# 프로그래머스 131704: 택배상자

def solution(order):
    answer = 0
    container = []
    i, j = 1, 0

    while True:
        while i == order[j]:
            answer += 1
            i += 1
            j += 1

        while len(container) > 0 and container[-1] == order[j]:
            container.pop()
            answer += 1
            j += 1
        
        if i > len(order):
            break
        
        container.append(i)
        i += 1

    return answer