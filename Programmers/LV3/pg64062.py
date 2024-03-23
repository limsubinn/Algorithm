# 프로그래머스 64062: 징검다리 건너기

from collections import deque

def solution(stones, k):
    # 징검다리의 길이가 k 이하일 경우
    if len(stones) <= k:
        return max(stones)

    # 슬라이딩 윈도우
    queue = deque()
    for i in range(k):
        # 의미 없는 값 빼기
        while queue and queue[-1][1] < stones[i]:
            queue.pop()
        # 현재 값 넣기
        queue.append((i, stones[i]))

    answer = queue[0][1]  # 최댓값

    for i in range(k, len(stones)):
        # 맨 앞 원소 빼기
        if queue[0][0] == i - k:
            queue.popleft()
        # 의미 없는 값 빼기
        while queue and queue[-1][1] < stones[i]:
            queue.pop()
        # 현재 값 넣기
        queue.append((i, stones[i]))
        # 정답 갱신
        answer = min(answer, queue[0][1])

    return answer