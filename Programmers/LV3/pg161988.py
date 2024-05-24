# 프로그래머스 161988: 연속 펄스 부분 수열의 합

def find_max(s):
    for i in range(1, len(s)):
        s[i] = max(s[i], s[i - 1] + s[i])
    return max(s)

def solution(sequence):
    # [1, -1, 1, ...]
    s1 = [(sequence[i] if i % 2 == 0 else -sequence[i]) for i in range(len(sequence))]
    # [-1, 1, -1, ...]
    s2 = [(sequence[i] if i % 2 != 0 else -sequence[i]) for i in range(len(sequence))]
    # 가장 큰 부분 수열의 합 찾기
    answer = max(find_max(s1), find_max(s2))
    return answer