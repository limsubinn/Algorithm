# 프로그래머스 42746: 가장 큰 수

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x:(x*4)[:4], reverse=True)
    
    answer = ''.join(numbers)
    if int(answer) == 0:
        answer = '0'
    return answer