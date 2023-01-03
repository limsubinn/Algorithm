# 프로그래머스 81301: 숫자 문자열과 영단어

def solution(s):
    num = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    for i in range(10):
        if num[i] in s:
            s = s.replace(num[i], str(i))

    return int(s)