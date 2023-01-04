# 프로그래머스 86051: 없는 숫자 더하기 (Python)

def solution(numbers):
    answer = 0
    numbers.sort()

    for i in range(1, 10):
        if i not in numbers:
            answer += i

    return answer