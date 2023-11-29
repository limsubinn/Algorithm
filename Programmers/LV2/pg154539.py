# 프로그래머스 154539: 뒤에 있는 큰 수 찾기

def solution(numbers):
    answer = [-1] * len(numbers)
    s = []

    for i in range(len(numbers)):
        while s and numbers[s[-1]] < numbers[i]:
            answer[s.pop()] = numbers[i]
        s.append(i)

    return answer

'''
시간초과 (이중반복문,,)

def solution(numbers):
    answer = []
    for i in range(len(numbers)-1):
        for j in numbers[i+1 : len(numbers)]:
            if j > numbers[i]:
                answer.append(j)
                break
        else:
            answer.append(-1)
    answer.append(-1)
    return answer
'''