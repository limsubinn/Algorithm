# 프로그래머스 178870: 연속된 부분 수열의 합

def solution(sequence, k):
    j = 0
    s = sequence[0] # 부분 수열의 합
    l = 1_000_001 # 수열 길이의 최댓값
    answer = [0, 0]

    # 왼쪽 포인터 이동
    for i in range(len(sequence)):
        # 오른쪽 포인터 이동
        while s < k and j < len(sequence) - 1:
            j += 1
            s += sequence[j]

        # 정답 갱신
        if s == k and j - i < l:
            l = j - i
            answer = [i, j]

        s -= sequence[i]

    return answer