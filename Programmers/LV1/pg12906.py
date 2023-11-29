# 프로그래머스 12906: 같은 숫자는 싫어

def solution(arr):
    answer = []

    while arr:
        a = arr.pop()
        if answer and a == answer[-1]:
            continue
        answer.append(a)
 
    return answer[::-1]