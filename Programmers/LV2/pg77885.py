# 프로그래머스 77885: 2개 이하로 다른 비트

def findOddAnswer(number):
    # 2진수 변환
    b = '0' + str(bin(number))[2:]

    # 맨 마지막 0 인덱스 찾기
    i = b.rindex('0')

    # 숫자 변환
    b = list(b)
    b[i] = '1'
    b[i + 1] = '0'

    # 10진수로 변환
    return int(''.join(b), 2)


def solution(numbers):
    answer = []

    for number in numbers:
        # 짝수
        if number % 2 == 0:
            answer.append(number + 1)
        # 홀수
        else:
            answer.append(findOddAnswer(number))

    return answer