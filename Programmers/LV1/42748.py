# 프로그래머스 42748: K번째 수 

def solution(array, commands):
    answer = []
    for i, j, k in commands:
        arr = array[i-1:j]
        answer.append(sorted(arr)[k-1])
    return answer