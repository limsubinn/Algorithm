# 프로그래머스 42583: 다리를 지나는 트럭

from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0], maxlen=bridge_length)
    size = 0
    
    for i in truck_weights:
        while (size + i - bridge[0] > weight):
            size -= bridge[0]
            bridge.append(0)
            answer += 1
        
        size -= bridge[0]
        bridge.append(i)
        size += i
        answer += 1
            
    return answer + bridge_length