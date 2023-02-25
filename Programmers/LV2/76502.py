# 프로그래머스 76502: 괄호 회전하기

from collections import deque

def solution(s):
    answer = 0
    s = deque(s, maxlen=len(s))

    small = "()"
    medium = "{}"
    large = "[]"

    for i in range(len(s)):
        s.append(s[0])
        temp = "".join(list(s))

        while small in temp or medium in temp or large in temp:
            temp = temp.replace(small, "")
            temp = temp.replace(medium, "")
            temp = temp.replace(large, "")

        if len(temp) == 0:
            answer += 1

    return answer