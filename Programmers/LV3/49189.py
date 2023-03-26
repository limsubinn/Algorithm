# 프로그래머스 49189: 가장 먼 노드

from collections import deque

def solution(n, edge):
    # 연결된 노드 저장
    array = [[] for i in range(n+1)]
    for i, j in edge:
        array[i].append(j)
        array[j].append(i)

    queue = deque()
    queue.append([array[1], 1])
    result = [0] * 2 + [20000] * (n-1) # 거리를 저장할 배열
    
    while queue:
        arr, distance = queue.popleft()
        for i in arr:
            if result[i] == 20000: # 노드에 방문한 적이 없을 때
                result[i] = distance
                queue.append([array[i], distance + 1])
            
    m = max(result)
    answer = result.count(m)
        
    return answer